from datetime import datetime
from typing import Any, Dict
from unittest.mock import AsyncMock, patch

import pytest

from valopy.client import Client
from valopy.enums import Platform, Region
from valopy.exceptions import ValoPyValidationError
from valopy.models import (
    Leaderboard,
    LeaderboardPlayer,
    LeaderboardThreshold,
    Result,
    ResultMetadata,
)
from valopy.utils import dict_to_dataclass


class TestLeaderboard:
    """Test Leaderboard endpoint."""

    @pytest.mark.asyncio
    async def test_get_leaderboard_parsing(self, leaderboard: Dict[str, Any]) -> None:
        """Test that Leaderboard response is correctly parsed with metadata.

        Parameters
        ----------
        leaderboard : Dict[str, Any]
            Mock leaderboard response data with results metadata.
        """

        client = Client(api_key="test-key")

        leaderboard_data = dict_to_dataclass(leaderboard["data"], Leaderboard)

        with patch.object(client.adapter, "get", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = Result(status_code=200, message="OK", data=leaderboard_data)

            result: Leaderboard = await client.get_leaderboard(
                region=Region.NA, platform=Platform.PC
            )

            # Verify main data
            assert isinstance(result, Leaderboard)
            assert type(result.updated_at) is datetime
            assert len(result.players) > 0
            assert len(result.thresholds) > 0

            # Verify subdataclasses
            assert isinstance(result.thresholds[0], LeaderboardThreshold)
            assert isinstance(result.players[0], LeaderboardPlayer)

            # Verify results metadata is in the data
            assert isinstance(result.results, ResultMetadata)
            assert result.results.total == leaderboard["data"]["results"]["total"]

        await client.close()

    @pytest.mark.asyncio
    async def test_get_leaderboard_validation_error(self) -> None:
        """Test validation error when both puuid and name are provided."""

        client = Client(api_key="test-key")

        with pytest.raises(ValoPyValidationError) as exc_info:
            await client.get_leaderboard(
                region=Region.NA,
                platform=Platform.PC,
                puuid="test-puuid",
                name="TestPlayer",
                tag="TAG",
            )

        assert "Cannot filter by both puuid and name/tag" in str(exc_info.value)

        await client.close()
