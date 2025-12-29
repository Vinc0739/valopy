import logging
import types
from typing import TYPE_CHECKING, Optional

from .adapter import Adapter
from .enums import CountryCode, Endpoint, Locale, Region

if TYPE_CHECKING:
    import types

    from .models import AccountV1, AccountV2, Content, QueueData, Status, Version, WebsiteContent

_log = logging.getLogger(__name__)


class Client:
    """Client for interacting with the Valorant API.

    Attributes
    ----------
    adapter : Adapter
        The adapter used for making HTTP requests.
    """

    def __init__(self, api_key: str, redact_header: bool = True) -> None:
        """Initialize the Client.

        Parameters
        ----------
        api_key : str
            The API key used for authentication.
        redact_header : bool, optional
            Whether to redact the API key in logs, by default True
        """

        _log.info("Initializing Valorant API Client (redact_header=%s)", redact_header)
        _log.debug("Creating adapter with provided API key")

        self.adapter = Adapter(api_key=api_key, redact_header=redact_header)

    async def close(self) -> None:
        """Close the client's adapter session.

        Returns
        -------
        None
        """
        await self.adapter.close()

    async def __aenter__(self) -> "Client":
        """Async context manager entry.

        Returns
        -------
        Client
            The client instance.
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

    async def get_account_v1(self, name: str, tag: str, force_update: bool = False) -> "AccountV1":
        """Get Account V1 information.

        Parameters
        ----------
        name : str
            The name of the account.
        tag : str
            The tag of the account.
        force_update : bool, optional
            Whether to force update the account information, by default False

        Returns
        -------
        AccountV1
            The Account V1 information.
        """

        _log.info("Fetching Account V1 for %s#%s", name, tag)
        if force_update:
            _log.debug("Force update enabled for account %s#%s", name, tag)

        endpoint_path = Endpoint.ACCOUNT_BY_NAME_V1.url.format(name=name, tag=tag)

        result = await self.adapter.get(
            endpoint_path=endpoint_path,
            params={"force": str(force_update).lower()},
            model_class=Endpoint.ACCOUNT_BY_NAME_V1.model,
        )

        _log.info("Successfully retrieved Account V1 for %s#%s", name, tag)
        return result.data  # type: ignore

    async def get_account_v1_by_puuid(self, puuid: str, force_update: bool = False) -> "AccountV1":
        """Get Account V1 information by PUUID.

        Parameters
        ----------
        puuid : str
            The player's unique identifier (PUUID).
        force_update : bool, optional
            Whether to force update the account information, by default False

        Returns
        -------
        AccountV1
            The Account V1 information.
        """

        _log.info("Fetching Account V1 by PUUID %s", puuid)
        if force_update:
            _log.debug("Force update enabled for account PUUID %s", puuid)

        endpoint_path = Endpoint.ACCOUNT_BY_PUUID_V1.url.format(puuid=puuid)

        result = await self.adapter.get(
            endpoint_path=endpoint_path,
            params={"force": str(force_update).lower()},
            model_class=Endpoint.ACCOUNT_BY_PUUID_V1.model,
        )

        _log.info("Successfully retrieved Account V1 for PUUID %s", puuid)
        return result.data  # type: ignore

    async def get_account_v2(self, name: str, tag: str, force_update: bool = False) -> "AccountV2":
        """Get Account V2 information.

        Parameters
        ----------
        name : str
            The name of the account.
        tag : str
            The tag of the account.
        force_update : bool, optional
            Whether to force update the account information, by default False

        Returns
        -------
        AccountV2
            The Account V2 information.
        """

        _log.info("Fetching Account V2 for %s#%s", name, tag)
        if force_update:
            _log.debug("Force update enabled for account %s#%s", name, tag)

        endpoint_path = Endpoint.ACCOUNT_BY_NAME_V2.url.format(name=name, tag=tag)

        result = await self.adapter.get(
            endpoint_path=endpoint_path,
            params={"force": str(force_update).lower()},
            model_class=Endpoint.ACCOUNT_BY_NAME_V2.model,
        )

        _log.info("Successfully retrieved Account V2 for %s#%s", name, tag)
        return result.data  # type: ignore

    async def get_account_v2_by_puuid(self, puuid: str, force_update: bool = False) -> "AccountV2":
        """Get Account V2 information by PUUID.

        Parameters
        ----------
        puuid : str
            The player's unique identifier (PUUID).
        force_update : bool, optional
            Whether to force update the account information, by default False

        Returns
        -------
        AccountV2
            The Account V2 information.
        """

        _log.info("Fetching Account V2 by PUUID %s", puuid)
        if force_update:
            _log.debug("Force update enabled for account PUUID %s", puuid)

        endpoint_path = Endpoint.ACCOUNT_BY_PUUID_V2.url.format(puuid=puuid)

        result = await self.adapter.get(
            endpoint_path=endpoint_path,
            params={"force": str(force_update).lower()},
            model_class=Endpoint.ACCOUNT_BY_PUUID_V2.model,
        )

        _log.info("Successfully retrieved Account V2 for PUUID %s", puuid)
        return result.data  # type: ignore

    async def get_content(self, locale: Optional[Locale] = None) -> "Content":
        """Get basic content data like season ids or skins.

        Parameters
        ----------
        locale : Optional[Locale], optional
            The locale for the content data, by default None

        Returns
        -------
        Content
            The content data retrieved from the API.
        """

        _log.info("Fetching content data (locale=%s)", locale or "default")

        params = {"locale": locale.value} if locale else {}

        result = await self.adapter.get(
            endpoint_path=Endpoint.CONTENT_V1.url,
            params=params,
            model_class=Endpoint.CONTENT_V1.model,
        )

        _log.info("Successfully retrieved content data")

        return result.data  # type: ignore

    async def get_version(self, region: Optional[Region] = Region.EU) -> "Version":
        """Get the current API version for a specific region.

        Parameters
        ----------
        region : Optional[Region], optional
            The region to get the API version for, by default Region.EU

        Returns
        -------
        Version
            The version data retrieved from the API.
        """

        _log.info("Fetching Version for region %s", region.value)

        endpoint_path = Endpoint.VERSION_V1.url.format(region=region.value)

        result = await self.adapter.get(
            endpoint_path=endpoint_path,
            model_class=Endpoint.VERSION_V1.model,
        )

        _log.info("Successfully retrieved Version for region %s", region.value)

        return result.data  # type: ignore

    async def get_website(self, countrycode: CountryCode) -> list["WebsiteContent"]:
        """Get website information for a specific country code.

        Parameters
        ----------
        countrycode : CountryCodes
            The country code to get the website information for.

        Returns
        -------
        Website
            The website information.
        """

        _log.info("Fetching Website for country code %s", countrycode.value)

        endpoint_path = Endpoint.WEBSITE.url.format(countrycode=countrycode.value)

        result = await self.adapter.get(
            endpoint_path=endpoint_path,
            model_class=Endpoint.WEBSITE.model,
        )

        return result.data  # type: ignore

    async def get_status(self, region: Region) -> "Status":
        """Get the current VALORANT server status for a region.

        Parameters
        ----------
        region : Region
            The region to get server status for.

        Returns
        -------
        Status
            The server status including maintenances and incidents.
        """

        _log.info("Fetching server status for region %s", region.value)

        endpoint_path = Endpoint.STATUS.url.format(region=region.value)

        result = await self.adapter.get(
            endpoint_path=endpoint_path,
            model_class=Endpoint.STATUS.model,
        )

        _log.info("Successfully retrieved server status for region %s", region.value)

        return result.data  # type: ignore

    async def get_queue_status(self, region: Region) -> list["QueueData"]:
        """Get the current queue status for a region.

        Parameters
        ----------
        region : Region
            The region to get queue status for.

        Returns
        -------
        list[QueueData]
            List of queue configurations for all available game modes.
        """

        _log.info("Fetching queue status for region %s", region.value)

        endpoint_path = Endpoint.QUEUE_STATUS.url.format(region=region.value)

        result = await self.adapter.get(
            endpoint_path=endpoint_path,
            model_class=Endpoint.QUEUE_STATUS.model,
        )

        _log.info("Successfully retrieved queue status for region %s", region.value)

        return result.data  # type: ignore
