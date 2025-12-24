import logging
from typing import TYPE_CHECKING, Optional, Type

import aiohttp

from .enums import AllowedMethods
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
    api_key : str
        The API key used for authentication.
    api_url : str
        The base URL for the Valorant API.
    """

    def __init__(self, api_key: str, redact_header: bool = True) -> None:
        """Initialize the Adapter.

        Parameters
        ----------
        api_key : str
            The API key used for authentication.
        redact_header : bool, optional
            Whether to redact the API key in logs, by default True
        """

        self.api_url = "https://api.henrikdev.xyz/valorant"
        self.redact_header = redact_header

        self._api_key = api_key
        self._session: Optional[aiohttp.ClientSession] = None

        _log.info("Adapter initialized with API URL: %s (redact_header=%s)", self.api_url, redact_header)
        _log.debug("Adapter ready for making requests")

    async def _get_session(self) -> aiohttp.ClientSession:
        """Get or create the persistent aiohttp session.

        Returns
        -------
        aiohttp.ClientSession
            The persistent session for making requests.
        """

        if self._session is None or self._session.closed:
            _log.info("Creating new aiohttp ClientSession")

            self._session = aiohttp.ClientSession()

        else:
            _log.debug("Reusing existing aiohttp ClientSession")

        return self._session

    async def close(self) -> None:
        """Close the persistent session.

        Returns
        -------
        None
        """
        if self._session and not self._session.closed:
            _log.info("Closing aiohttp ClientSession")

            await self._session.close()

        else:
            _log.debug("Session already closed or was never created")

    async def __aenter__(self) -> "Adapter":
        """Async context manager entry.

        Returns
        -------
        Adapter
            The adapter instance.
        """
        return self

    async def __aexit__(
        self,
        exc_type: "type[BaseException] | None",
        exc_val: "BaseException | None",
        exc_tb: "types.TracebackType | None",
    ) -> None:
        """Async context manager exit.

        Parameters
        ----------
        exc_type : type[BaseException] | None
            Exception type if raised.
        exc_val : BaseException | None
            Exception value if raised.
        exc_tb : types.TracebackType | None
            Exception traceback if raised.

        Returns
        -------
        None
        """

        await self.close()

    async def _do(
        self,
        method: AllowedMethods,
        endpoint_path: str,
        model_class: Type[ValoPyModel],
        params: dict | None = None,
    ) -> Result:
        """Make an HTTP request to the Valorant API.

        Parameters
        ----------
        method : AllowedMethods
            The HTTP method to use for the request.
        endpoint_path : str
            The formatted API endpoint path to call.
        model_class : Type[APIModel]
            The dataclass type to deserialize the response into
        params : dict | None, optional
            Query parameters to include in the request, by default None

        Returns
        -------
        Result
            The result of the HTTP request.

        Raises
        ------
        ValoPyRequestError
            If a 400 Bad Request error occurs.
        ValoPyPermissionError
            If a 401 Permission Denied error occurs.
        ValoPyNotFoundError
            If a 404 Not Found error occurs.
        ValoPyTimeoutError
            If a 408 Request Timeout error occurs.
        ValoPyRateLimitError
            If a 429 Rate Limit Exceeded error occurs.
        ValoPyServerError
            If a 5xx Server Error occurs.
        ValoPyHTTPError
            For other HTTP errors.
        aiohttp.ClientError
            For other client errors.
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
                "HTTP error %d on %s request to endpoint %s", e.status, method.value, endpoint_path, exc_info=True
            )

            raise from_client_response_error(error=e, redacted=self.redact_header) from e

        except aiohttp.ClientError as e:
            _log.error("Client error on %s request to %s: %s", method.value, url, str(e), exc_info=True)

            raise

        # Parse response data
        data = await response.json()

        _log.debug(
            "%s request completed with status %d",
            method.value,
            response.status,
        )

        # Extract the actual data from the response
        response_data = data.get("data", {})

        _log.info("Received response data from %s (size: %d bytes)", endpoint_path, len(str(response_data)))

        if not isinstance(response_data, dict):
            _log.warning("Response data is not a dict, cannot convert to dataclass")

        else:
            _log.info("Converting response to %s dataclass for endpoint %s", model_class.__name__, endpoint_path)

            # Convert dict to dataclass
            response_data = dict_to_dataclass(data=response_data, dataclass_type=model_class)

        return Result(
            status_code=response.status,
            message=response.reason or "OK",
            data=response_data,
        )

    async def get(self, endpoint_path: str, model_class: Type[ValoPyModel], params: dict | None = None) -> Result:
        """Make a GET request to the Valorant API.

        Parameters
        ----------
        endpoint_path : str
            The formatted API endpoint path to call.
        model_class : Type[ValoPyModel]
            The dataclass type to deserialize the response into
        params : dict | None, optional
            Query parameters to include in the request, by default None

        Returns
        -------
        Result
            The result of the GET request.
        """

        return await self._do(
            method=AllowedMethods.GET, endpoint_path=endpoint_path, params=params, model_class=model_class
        )

    async def post(self, endpoint_path: str, model_class: Type[ValoPyModel], params: dict | None = None) -> Result:
        """Make a POST request to the Valorant API.

        Parameters
        ----------
        endpoint_path : str
            The formatted API endpoint path to call.
        model_class : Type[ValoPyModel]
            The dataclass type to deserialize the response into
        params : dict | None, optional
            Query parameters to include in the request, by default None

        Returns
        -------
        Result
            The result of the POST request.
        """

        return await self._do(
            method=AllowedMethods.POST, endpoint_path=endpoint_path, params=params, model_class=model_class
        )
