import logging
from typing import TYPE_CHECKING, Optional, Type

import aiohttp

from .enums import AllowedMethod
from .exceptions import from_client_response_error
from .models import Result, ValoPyModel
from .utils import dict_to_dataclass

if TYPE_CHECKING:
    import types

_log = logging.getLogger(__name__)


class Adapter:
    """Adapter for making HTTP requests to the Valorant API.

    This adapter provides automatic model typing and elegant error handling
    for all Valorant API endpoints.

    Attributes
    ----------
    api_key : :class:`str`
        The API key used for authentication.
    api_url : :class:`str`
        The base URL for the Valorant API.
    """

    def __init__(self, api_key: str, redact_header: bool = True) -> None:
        """Initialize the Adapter.

        Parameters
        ----------
        api_key : :class:`str`
            The API key used for authentication.
        redact_header : Optional[:class:`bool`]
            Whether to redact the API key in logs, by default True
        """

        self.api_url = "https://api.henrikdev.xyz/valorant"
        self.redact_header = redact_header

        self._api_key = api_key
        self._session: Optional[aiohttp.ClientSession] = None

        _log.info(
            "Adapter initialized with API URL: %s (redact_header=%s)",
            self.api_url,
            redact_header,
        )
        _log.debug("Adapter ready for making requests")

    async def _get_session(self) -> aiohttp.ClientSession:
        """Get or create the persistent aiohttp session.

        Returns
        -------
        :class:`aiohttp.ClientSession`
            The persistent session for making requests.
        """

        if self._session is None or self._session.closed:
            _log.info("Creating new aiohttp ClientSession")

            self._session = aiohttp.ClientSession()

        else:
            _log.debug("Reusing existing aiohttp ClientSession")

        return self._session

    async def close(self) -> None:
        """Close the persistent session."""

        if self._session and not self._session.closed:
            _log.info("Closing aiohttp ClientSession")

            await self._session.close()

        else:
            _log.debug("Session already closed or was never created")

    async def __aenter__(self) -> "Adapter":
        """Async context manager entry.

        Returns
        -------
        :class:`Adapter`
            The adapter instance.
        """
        return self

    async def __aexit__(
        self,
        exc_type: "Type[BaseException] | None",
        exc_val: "BaseException | None",
        exc_tb: "types.TracebackType | None",
    ) -> None:
        """Async context manager exit.

        Parameters
        ----------
        exc_type : Optional[type[:class:`BaseException`]]
            Exception type if raised.
        exc_val : Optional[:class:`BaseException`]
            Exception value if raised.
        exc_tb : Optional[:class:`types.TracebackType`]
            Exception traceback if raised.
        """

        await self.close()

    async def _do(
        self,
        method: AllowedMethod,
        endpoint_path: str,
        model_class: Type[ValoPyModel],
        params: Optional[dict] = None,
    ) -> Result:
        """Make an HTTP request to the Valorant API.

        Parameters
        ----------
        method : :class:`AllowedMethod`
            The HTTP method to use for the request.
        endpoint_path : :class:`str`
            The formatted API endpoint path to call.
        model_class : Type[:class:`APIModel`]
            The dataclass type to deserialize the response into
        params : Optional[:class:`dict`]
            Query parameters to include in the request, by default None

        Returns
        -------
        :class:`Result`
            A Result object containing the HTTP response metadata and deserialized data.

        Raises
        ------
        :exc:`ValoPyRequestError`
            Raised when a 400 Bad Request error occurs, typically indicating invalid parameters.
        :exc:`ValoPyPermissionError`
            Raised when a 401 Unauthorized error occurs, indicating invalid or missing API key.
        :exc:`ValoPyNotFoundError`
            Raised when a 404 Not Found error occurs, indicating the resource does not exist.
        :exc:`ValoPyTimeoutError`
            Raised when a 408 Request Timeout error occurs, indicating the request took too long.
        :exc:`ValoPyRateLimitError`
            Raised when a 429 Too Many Requests error occurs, indicating rate limit exceeded.
        :exc:`ValoPyServerError`
            Raised when a 5xx Server Error occurs, indicating an issue with the API server.
        :exc:`ValoPyHTTPError`
            Raised for other HTTP errors not covered by specific exception types.
        :exc:`aiohttp.ClientError`
            Raised for client-level errors such as connection issues or network problems.
        """

        # Construct the full URL and headers
        url = f"{self.api_url}{endpoint_path}"
        headers = {"accept": "application/json", "Authorization": self._api_key}

        # Get the session
        session = await self._get_session()

        try:
            # Log request initiation
            _log.info(
                "Starting %s request to endpoint: %s",
                method.value,
                endpoint_path,
            )
            _log.debug(
                "API Key: %s Full URL: %s (params=%s)",
                self._api_key if not self.redact_header else "[REDACTED]",
                url,
                params,
            )

            # Make the HTTP request
            response = await session.request(
                method=method.value,
                url=url,
                headers=headers,
                params=params,
            )

            # Check for HTTP errors
            response.raise_for_status()
            _log.debug("HTTP %d response received", response.status)

        except aiohttp.ClientResponseError as e:
            _log.error(
                "HTTP error %d on %s request to endpoint %s",
                e.status,
                method.value,
                endpoint_path,
                exc_info=True,
            )

            raise from_client_response_error(error=e, redacted=self.redact_header) from e

        except aiohttp.ClientError as e:
            _log.error(
                "Client error on %s request to %s: %s", method.value, url, str(e), exc_info=True
            )

            raise

        # Parse response data
        data = await response.json()

        _log.debug(
            "%s request completed with status %d",
            method.value,
            response.status,
        )

        # Extract results metadata if present
        results_metadata = data.get("results")

        # Extract the actual data from the response
        response_data = data.get("data", {})

        _log.info(
            "Received response data from %s (size: %d bytes)",
            endpoint_path,
            len(str(response_data)),
        )

        if isinstance(response_data, list):
            _log.info(
                "Converting list response to %s dataclass for endpoint %s",
                model_class.__name__,
                endpoint_path,
            )

            # Convert list of dicts to list of dataclasses
            response_data = [
                dict_to_dataclass(data=item, dataclass_type=model_class)
                for item in response_data
                if isinstance(item, dict)
            ]

        elif isinstance(response_data, dict):
            # Inject results metadata into response dict before deserialization if present
            if results_metadata:
                response_data["results"] = results_metadata
                _log.debug("Added results metadata to response data")

            _log.info(
                "Converting response to %s dataclass for endpoint %s",
                model_class.__name__,
                endpoint_path,
            )

            # Convert dict to dataclass (results will be deserialized if present)
            response_data = dict_to_dataclass(data=response_data, dataclass_type=model_class)

        else:
            _log.warning("Response data is not a dict or list, cannot convert to dataclass")

        return Result(
            status_code=response.status,
            message=response.reason or "OK",
            data=response_data,
        )

    async def get(
        self,
        endpoint_path: str,
        model_class: Type[ValoPyModel],
        params: Optional[dict] = None,
    ) -> Result:
        """Make a GET request to the Valorant API.

        Parameters
        ----------
        endpoint_path : class:`str`
            The formatted API endpoint path to call.
        model_class : Type[:class:`ValoPyModel`]
            The dataclass type to deserialize the response into
        params : Optional[class:`dict`]
            Query parameters to include in the request, by default None

        Returns
        -------
        :class:`Result`
            The result of the GET request.
        """

        return await self._do(
            method=AllowedMethod.GET,
            endpoint_path=endpoint_path,
            params=params,
            model_class=model_class,
        )

    async def post(
        self,
        endpoint_path: str,
        model_class: Type[ValoPyModel],
        params: Optional[dict] = None,
    ) -> Result:
        """Make a POST request to the Valorant API.

        Parameters
        ----------
        endpoint_path : class:`str`
            The formatted API endpoint path to call.
        model_class : Type[:class:`ValoPyModel`]
            The dataclass type to deserialize the response into
        params : Optional[class:`dict`]
            Query parameters to include in the request, by default None

        Returns
        -------
        :class:`Result`
            The result of the POST request.
        """

        return await self._do(
            method=AllowedMethod.POST,
            endpoint_path=endpoint_path,
            params=params,
            model_class=model_class,
        )
