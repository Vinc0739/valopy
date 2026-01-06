import logging
import types
from typing import TYPE_CHECKING, Optional

from .adapter import Adapter
from .enums import CountryCode, Endpoint, EsportsRegion, League, Locale, Platform, Region, Season
from .exceptions import ValoPyValidationError

if TYPE_CHECKING:
    import types

    from .models import (
        AccountV1,
        AccountV2,
        Content,
        EsportsEvent,
        Leaderboard,
        QueueData,
        Status,
        Version,
        WebsiteContent,
    )

_log = logging.getLogger(__name__)


class Client:
    """Client for interacting with the Valorant API.

    Attributes
    ----------
    adapter : :class:`~valopy.adapter.Adapter`
        The adapter used for making HTTP requests.
    """

    def __init__(self, api_key: str, redact_header: bool = True) -> None:
        """Initialize the Client.

        Parameters
        ----------
        api_key : :class:`str`
            The API key used for authentication.
        redact_header : :class:`bool`, default True
            Whether to redact the API key in logs, by default True
        """

        _log.info("Initializing Valorant API Client (redact_header=%s)", redact_header)
        _log.debug("Creating adapter with provided API key")

        self.adapter = Adapter(api_key=api_key, redact_header=redact_header)

    async def close(self) -> None:
        """Close the client's adapter session."""

        await self.adapter.close()

    async def __aenter__(self) -> "Client":
        """Async context manager entry.

        Returns
        -------
        :class:`Client`
            The client instance.
        """
        return self

    async def __aexit__(
        self,
        exc_type: "Optional[type[BaseException]]",
        exc_val: "Optional[BaseException]",
        exc_tb: "Optional[types.TracebackType]",
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

    async def get_account_v1(self, name: str, tag: str, force_update: bool = False) -> "AccountV1":
        """Get Account V1 information.

        Parameters
        ----------
        name : :class:`str`
            The name of the account.
        tag : :class:`str`
            The tag of the account.
        force_update : :class:`bool`, default False
            Whether to force update the account information, by default False

        Returns
        -------
        :class:`~valopy.models.AccountV1`
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
        puuid : :class:`str`
            The player's unique identifier (PUUID).
        force_update : :class:`bool`, default False
            Whether to force update the account information, by default False

        Returns
        -------
        :class:`~valopy.models.AccountV1`
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
        name : :class:`str`
            The name of the account.
        tag : :class:`str`
            The tag of the account.
        force_update : :class:`bool`, default false
            Whether to force update the account information, by default False

        Returns
        -------
        :class:`~valopy.models.AccountV2`
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
        puuid : :class:`str`
            The player's unique identifier (PUUID).
        force_update : :class:`bool`, default false
            Whether to force update the account information, by default False

        Returns
        -------
        :class:`~valopy.models.AccountV2`
            The Account V2 information.
        """

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
        locale : Optional[:class:`Locale`]
            The locale for the content data, by default None

        Returns
        -------
        :class:`~valopy.models.Content`
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
        region : Optional[:class:`Region`]
            The region to get the API version for, by default Region.EU

        Returns
        -------
        :class:`~valopy.models.Version`
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
        countrycode : :class:`CountryCode`
            The country code to get the website information for.

        Returns
        -------
        list[:class:`~valopy.models.WebsiteContent`]
            A list of website content data.
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
        region : :class:`Region`
            The region to get server status for.

        Returns
        -------
        :class:`~valopy.models.Status`
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
        region : :class:`Region`
            The region to get queue status for.

        Returns
        -------
        List[:class:`~valopy.models.QueueData`]
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

    async def get_esports_schedule(
        self, region: Optional[EsportsRegion] = None, league: Optional[League] = None
    ) -> list["EsportsEvent"]:
        """Get the esports schedule.

        Parameters
        ----------
        region : Optional[:class:`EsportsRegion`]
            Filter by esports region.
        league : Optional[:class:`League`]
            Filter by esports league.

        Returns
        -------
        List[:class:`~valopy.models.EsportsEvent`]
            List of esports events.
        """

        _log.info("Fetching esports schedule (region=%s, league=%s)", region, league)

        endpoint_path = Endpoint.ESPORTS_SCHEDULE.url

        params = {}
        if region:
            params["region"] = region.value
        if league:
            params["league"] = league.value
        result = await self.adapter.get(
            endpoint_path=endpoint_path,
            params=params,
            model_class=Endpoint.ESPORTS_SCHEDULE.model,
        )

        _log.info("Successfully retrieved esports schedule")

        return result.data  # type: ignore

    async def get_leaderboard(
        self,
        region: Region,
        platform: Platform,
        season: Optional[Season] = None,
        puuid: Optional[str] = None,
        name: Optional[str] = None,
        tag: Optional[str] = None,
        size: Optional[int] = None,
        start_index: Optional[int] = None,
    ) -> "Leaderboard":
        """Get leaderboard for a specific region and platform.

        Parameters
        ----------
        region : :class:`Region`
            The region to get leaderboard for.
        platform : :class:`Platform`
            The platform (PC or Console).
        season : Optional[:class:`Season`]
            The season to filter by (e.g., Season.E9A3).
        puuid : Optional[:class:`str`]
            Filter by player PUUID. Mutually exclusive with name and tag.
        name : Optional[:class:`str`]
            Filter by player name. Must be used with tag.
        tag : Optional[:class:`str`]
            Filter by player tag. Must be used with name.
        size : Optional[:class:`int`]
            Number of players to return.
        start_index : Optional[:class:`int`]
            Starting index for pagination.

        Returns
        -------
        :class:`~valopy.models.Leaderboard`
            Leaderboard data with players and pagination info.

        Raises
        ------
        :exc:`ValoPyValidationError`
            If both puuid and name/tag are provided,
            or if name is provided without tag (or vice versa).
        """

        # Validation: check that only puuid or name+tag is provided
        if puuid and (name or tag):
            raise ValoPyValidationError(
                "Cannot filter by both puuid and name/tag. Use only one of: puuid OR (name and tag)"
            )

        if (name and not tag) or (tag and not name):
            raise ValoPyValidationError(
                "Name and tag must both be provided together or both omitted"
            )

        _log.info(
            "Fetching leaderboard for region=%s, platform=%s, season=%s",
            region.value,
            platform.value,
            season,
        )

        endpoint_path = Endpoint.LEADERBOARD_V3.url.format(
            region=region.value, platform=platform.value
        )

        params = {}
        if season:
            params["season_short"] = season.value
        if puuid:
            params["puuid"] = puuid
        if name and tag:
            params["name"] = name
            params["tag"] = tag
        if size is not None:
            params["size"] = size
        if start_index is not None:
            params["start_index"] = start_index

        result = await self.adapter.get(
            endpoint_path=endpoint_path,
            params=params,
            model_class=Endpoint.LEADERBOARD_V3.model,
        )

        _log.info("Successfully retrieved leaderboard")

        return result.data  # type: ignore
