from typing import TYPE_CHECKING, Optional, Union

if TYPE_CHECKING:
    import aiohttp


class ValoPyError(Exception):
    """Base exception for all ValoPy errors."""


class ValoPyHTTPError(ValoPyError):
    """HTTP error with status code and URL information.

    Attributes
    ----------
    message : :class:`str`
        The error message describing the HTTP error.
    status_code : :class:`int`
        The HTTP status code.
    url : Optional[:class:`str`]
        The URL that caused the error, if available.
    """

    def __init__(self, message: str, status_code: int, url: Optional[str] = None) -> None:
        self.message = message
        self.status_code = status_code
        self.url = url

        super().__init__(f"({status_code}) {message}")


class ValoPyRequestError(ValoPyHTTPError):
    """Bad request (400).

    Attributes
    ----------
    message : :class:`str`
        Error message indicating bad request.
    status_code : :class:`int`
        HTTP status code (400).
    url : Optional[:class:`str`]
        The URL that caused the error.
    """

    def __init__(self, status_code: int, url: Optional[str] = None) -> None:
        self.message = f"Bad Request: {url}"
        self.status_code = status_code
        self.url = url

        super().__init__(message=self.message, status_code=status_code, url=url)


class ValoPyPermissionError(ValoPyHTTPError):
    """Permission denied (401).

    Attributes
    ----------
    message : :class:`str`
        Error message indicating permission denied.
    status_code : :class:`int`
        HTTP status code (401).
    url : Optional[:class:`str`]
        The URL that caused the error.
    request_headers : :class:`dict`
        The request headers from the failed request.
    """

    def __init__(
        self,
        status_code: int,
        url: Optional[str] = None,
        request_headers: dict = {},
        redacted: bool = False,
    ) -> None:

        api_key = request_headers.get("Authorization", "[REDACTED]")

        self.message = f"Permission Denied for KEY: {api_key}"
        self.status_code = status_code
        self.url = url

        super().__init__(message=self.message, status_code=status_code, url=url)


class ValoPyNotFoundError(ValoPyHTTPError):
    """Resource not found (404).

    Attributes
    ----------
    message : :class:`str`
        Error message indicating resource not found.
    status_code : :class:`int`
        HTTP status code (404).
    url : Optional[:class:`str`]
        The URL that was not found.
    """

    def __init__(self, status_code: int, url: Optional[str] = None) -> None:
        self.message = f"Not Found: {url}"
        self.status_code = status_code
        self.url = url

        super().__init__(message=self.message, status_code=status_code, url=url)


class ValoPyValidationError(ValoPyError):
    """Validation error for invalid parameter combinations.

    Attributes
    ----------
    message : :class:`str`
        The error message describing the validation error.
    """

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)


class ValoPyTimeoutError(ValoPyHTTPError):
    """Request timeout (408).

    Attributes
    ----------
    message : :class:`str`
        Error message indicating request timeout.
    status_code : :class:`int`
        HTTP status code (408).
    url : Optional[:class:`str`]
        The URL that timed out.
    """

    def __init__(self, status_code: int, url: Optional[str] = None) -> None:
        self.message = f"Request Timeout: {url}"
        self.status_code = status_code
        self.url = url

        super().__init__(status_code=status_code, message=self.message, url=url)


class ValoPyRateLimitError(ValoPyHTTPError):
    """Rate limit exceeded (429).

    Attributes
    ----------
    message : :class:`str`
        Error message indicating rate limit exceeded.
    status_code : :class:`int`
        HTTP status code (429).
    url : Optional[:class:`str`]
        The URL that exceeded the rate limit.
    rate_limit : Optional[:class:`str`]
        The rate limit value from response headers.
    rate_remain : Optional[:class:`str`]
        The remaining requests value from response headers.
    rate_reset : Optional[:class:`str`]
        The rate limit reset time from response headers.
    """

    def __init__(
        self, status_code: int, url: Optional[str] = None, response_headers: dict = {}
    ) -> None:
        self.rate_limit = response_headers.get("x-ratelimit-limit")
        self.rate_remain = response_headers.get("x-ratelimit-remaining")
        self.rate_reset = response_headers.get("x-ratelimit-reset")

        self.message = (
            f"Rate Limit Exceeded ({self.rate_remain}/{self.rate_limit}),"
            f"try again in {self.rate_reset}: {url}"
            if self.rate_limit
            else f"Rate Limit Exceeded: {url}"
        )

        self.status_code = status_code
        self.url = url

        super().__init__(message=self.message, status_code=status_code, url=url)


class ValoPyServerError(ValoPyHTTPError):
    """Server error (5xx).

    Attributes
    ----------
    message : :class:`str`
        Error message indicating server error.
    status_code : :class:`int`
        HTTP status code (5xx).
    url : Optional[:class:`str`]
        The URL that caused the server error.
    """

    def __init__(self, status_code: int, url: Optional[str] = None) -> None:
        self.message = f"Server Error: {url}"
        self.status_code = status_code
        self.url = url

        super().__init__(message=self.message, status_code=status_code, url=url)


def from_client_response_error(
    error: "aiohttp.ClientResponseError",
    redacted: bool,
) -> Union[
    ValoPyHTTPError,
    ValoPyRequestError,
    ValoPyPermissionError,
    ValoPyNotFoundError,
    ValoPyTimeoutError,
    ValoPyRateLimitError,
    ValoPyServerError,
]:
    """Convert an aiohttp ClientResponseError to a ValoPyHTTPError.

    Parameters
    ----------
    error : :class:`aiohttp.ClientResponseError`
        The original ClientResponseError.
    redacted : :class:`bool`
        Whether the API key in the request headers is redacted.

    Returns
    -------
    :exc:`ValoPyHTTPError` | :exc:`ValoPyRequestError` | :exc:`ValoPyPermissionError` | :exc:`ValoPyNotFoundError` | :exc:`ValoPyTimeoutError` | :exc:`ValoPyRateLimitError` | :exc:`ValoPyServerError`
        The corresponding ValoPy error matching the HTTP status code.

    Raises
    ------
    :exc:`ValoPyRequestError`
        If status code is 400.
    :exc:`ValoPyPermissionError`
        If status code is 401.
    :exc:`ValoPyNotFoundError`
        If status code is 404.
    :exc:`ValoPyTimeoutError`
        If status code is 408.
    :exc:`ValoPyRateLimitError`
        If status code is 429.
    :exc:`ValoPyServerError`
        If status code is 5xx.
    :exc:`ValoPyHTTPError`
        For any other HTTP error status codes.
    """  # noqa: E501

    request_headers = (
        dict(error.request_info.headers)
        if error.request_info and error.request_info.headers
        else {}
    )
    response_headers = dict(error.headers) if error.headers else {}

    match error.status:
        case 400:
            error_class = ValoPyRequestError(
                status_code=error.status,
                url=str(error.request_info.url) if error.request_info else None,
            )
        case 401:
            error_class = ValoPyPermissionError(
                status_code=error.status,
                url=str(error.request_info.url) if error.request_info else None,
                request_headers=request_headers if not redacted else {},
            )
        case 404:
            error_class = ValoPyNotFoundError(
                status_code=error.status,
                url=str(error.request_info.url) if error.request_info else None,
            )
        case 408:
            error_class = ValoPyTimeoutError(
                status_code=error.status,
                url=str(error.request_info.url) if error.request_info else None,
            )
        case 429:
            error_class = ValoPyRateLimitError(
                status_code=error.status,
                url=str(error.request_info.url) if error.request_info else None,
                response_headers=response_headers,
            )
        case status_code if 500 <= status_code < 600:
            error_class = ValoPyServerError(
                status_code=error.status,
                url=str(error.request_info.url) if error.request_info else None,
            )
        case _:
            error_class = ValoPyHTTPError(
                status_code=error.status,
                message=error.message,
                url=str(error.request_info.url) if error.request_info else None,
            )

    return error_class
