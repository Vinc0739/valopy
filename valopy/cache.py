import logging
import time
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from .enums import Endpoint

_log = logging.getLogger(__name__)


@dataclass
class EndpointCacheConfig:
    """Configuration for caching a specific endpoint.

    Attributes
    ----------
    enabled : :class:`bool`
        Whether caching is enabled for this endpoint.
    ttl : Optional[:class:`int`]
        Time-to-live in seconds for cached data. If None, uses default from CacheConfig.
    """

    enabled: bool = True
    ttl: Optional[int] = None


@dataclass
class CacheConfig:
    """Configuration for the caching system.

    Attributes
    ----------
    enabled : :class:`bool`, default True
        Whether caching is globally enabled.
    default_ttl : :class:`int`, default 3600
        Default time-to-live in seconds (1 hour) for cached data.
    endpoints : Dict["Endpoint", EndpointCacheConfig], optional
        Per-endpoint cache configurations. If an endpoint is not specified,
        it will use the default configuration with global default_ttl.
    """

    enabled: bool = True
    default_ttl: int = 3600  # 1 hour default
    endpoints: Dict["Endpoint", EndpointCacheConfig] = field(default_factory=dict)

    def get_endpoint_config(self, endpoint: "Endpoint") -> EndpointCacheConfig:
        """Get the cache configuration for a specific endpoint.

        Parameters
        ----------
        endpoint : :class:`Endpoint`
            The endpoint to get the configuration for.

        Returns
        -------
        :class:`~valopy.cache.EndpointCacheConfig`
            The cache configuration for the endpoint. If not explicitly defined,
            returns a default configuration using the global default_ttl.
        """

        if endpoint in self.endpoints:
            return self.endpoints[endpoint]

        # Return default configuration
        return EndpointCacheConfig()

    def is_endpoint_cached(self, endpoint: "Endpoint") -> bool:
        """Check if an endpoint is cached.

        Parameters
        ----------
        endpoint : :class:`Endpoint`
            The endpoint to check.

        Returns
        -------
        :class:`bool`
            True if caching is globally enabled and the endpoint is enabled.
        """

        if not self.enabled:
            return False

        config = self.get_endpoint_config(endpoint)
        return config.enabled

    def get_endpoint_ttl(self, endpoint: "Endpoint") -> int:
        """Get the TTL for a specific endpoint.

        Parameters
        ----------
        endpoint : :class:`Endpoint`
            The endpoint to get the TTL for.

        Returns
        -------
        :class:`int`
            The TTL in seconds. Uses endpoint-specific TTL if set,
            otherwise uses the global default_ttl.
        """

        config = self.get_endpoint_config(endpoint)
        if config.ttl is not None:
            return config.ttl

        return self.default_ttl


@dataclass
class CacheEntry:
    """A cached API response entry.

    Attributes
    ----------
    data : Any
        The cached response data.
    created_at : :class:`float`
        Timestamp when the entry was created (Unix time).
    ttl : :class:`int`
        Time-to-live in seconds.
    """

    data: Any
    created_at: float
    ttl: int

    def is_expired(self) -> bool:
        """Check if the cache entry has expired.

        Returns
        -------
        :class:`bool`
            True if the entry has expired, False otherwise.
        """

        return time.time() - self.created_at > self.ttl


class CacheManager:
    """Manages the caching system for API responses.

    This class handles cache storage, retrieval, and expiration.

    Attributes
    ----------
    config : :class:`CacheConfig`
        The cache configuration.
    """

    def __init__(self, config: CacheConfig) -> None:
        """Initialize the CacheManager.

        Parameters
        ----------
        config : :class:`CacheConfig`
            The cache configuration.
        """

        self.config = config
        self._cache: Dict[str, CacheEntry] = {}

        _log.info(
            "CacheManager initialized (enabled=%s, default_ttl=%ds)",
            config.enabled,
            config.default_ttl,
        )

        if config.endpoints:
            _log.debug(
                "Configured cache settings for %d endpoints",
                len(config.endpoints),
            )

    def _generate_cache_key(
        self,
        endpoint_path: str,
        params: Optional[Dict[str, Any]] = None,
    ) -> str:
        """Generate a cache key for a request.

        Parameters
        ----------
        endpoint_path : :class:`str`
            The formatted endpoint path (includes URL parameters).
        params : Optional[Dict[str, Any]]
            Query parameters.

        Returns
        -------
        :class:`str`
            The generated cache key.
        """

        # Convert params to a sorted string representation for consistent caching
        params_str = ""
        if params:
            params_str = "&".join(f"{k}={v}" for k, v in sorted(params.items()))

        cache_key = f"{endpoint_path}"
        if params_str:
            cache_key += f"?{params_str}"

        return cache_key

    def get(
        self,
        endpoint: "Endpoint",
        endpoint_path: str,
        params: Optional[Dict[str, Any]] = None,
    ) -> Optional[Any]:
        """Get a cached response.

        Parameters
        ----------
        endpoint : :class:`Endpoint`
            The endpoint enum.
        endpoint_path : :class:`str`
            The formatted endpoint path (includes URL parameters).
        params : Optional[Dict[str, Any]]
            Query parameters.

        Returns
        -------
        Optional[Any]
            The cached data if found and not expired, None otherwise.
        """

        # Check if caching is enabled for this endpoint
        if not self.config.is_endpoint_cached(endpoint):
            _log.debug("Caching disabled for endpoint %s", endpoint.name)
            return None

        cache_key = self._generate_cache_key(endpoint_path, params)

        if cache_key not in self._cache:
            _log.debug("Cache miss for key: %s", cache_key)
            return None

        entry = self._cache[cache_key]

        # Check if entry has expired
        if entry.is_expired():
            _log.debug("Cache entry expired for key: %s", cache_key)
            del self._cache[cache_key]
            return None

        _log.debug("Cache hit for key: %s", cache_key)
        return entry.data

    def set(
        self,
        endpoint: "Endpoint",
        endpoint_path: str,
        data: Any,
        params: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Cache a response.

        Parameters
        ----------
        endpoint : :class:`Endpoint`
            The endpoint enum.
        endpoint_path : :class:`str`
            The formatted endpoint path (includes URL parameters).
        data : Any
            The response data to cache.
        params : Optional[Dict[str, Any]]
            Query parameters.
        """

        # Check if caching is enabled for this endpoint
        if not self.config.is_endpoint_cached(endpoint):
            _log.debug("Caching disabled for endpoint %s", endpoint.name)
            return

        cache_key = self._generate_cache_key(endpoint_path, params)
        ttl = self.config.get_endpoint_ttl(endpoint)

        entry = CacheEntry(
            data=data,
            created_at=time.time(),
            ttl=ttl,
        )

        self._cache[cache_key] = entry
        _log.debug(
            "Cached response for key: %s (ttl=%ds)",
            cache_key,
            ttl,
        )

    def clear(self) -> None:
        """Clear all cached entries."""

        self._cache.clear()
        _log.info("Cache cleared")

    def clear_expired(self) -> None:
        """Remove all expired entries from the cache."""

        expired_keys = [key for key, entry in self._cache.items() if entry.is_expired()]

        for key in expired_keys:
            del self._cache[key]

        if expired_keys:
            _log.debug("Removed %d expired cache entries", len(expired_keys))

    def get_stats(self) -> Dict[str, Any]:
        """Get cache statistics.

        Returns
        -------
        Dict[str, Any]
            A dictionary containing cache statistics including:
            - total_entries: Total number of cached entries
            - expired_entries: Number of expired entries
            - active_entries: Number of non-expired entries
        """

        self.clear_expired()

        total = len(self._cache)
        expired = sum(1 for entry in self._cache.values() if entry.is_expired())
        active = total - expired

        return {
            "total_entries": total,
            "expired_entries": expired,
            "active_entries": active,
        }
