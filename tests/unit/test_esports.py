from datetime import datetime
from typing import Any, Dict, List
from unittest.mock import AsyncMock, patch

import pytest

from valopy.client import Client
from valopy.models import (
    EsportsEvent,
    EsportsGameType,
    EsportsLeague,
    EsportsTeam,
    EsportsTeamRecord,
    Result,
)
from valopy.utils import dict_to_dataclass


class TestEsports:
    """Test Esports Schedule endpoint."""

    @pytest.mark.asyncio
    async def test_get_esports_schedule_parsing(self, esports: Dict[str, Any]) -> None:
        """Test that Esports Schedule response is correctly parsed.

        Parameters
        ----------
        esports : Dict[str, Any]
            Mock esports response data.
        """

        client = Client(api_key="test-key")

        esports_data = [dict_to_dataclass(item, EsportsEvent) for item in esports["data"]]

        with patch.object(client.adapter, "get", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = Result(
                status_code=esports["status"], message="OK", data=esports_data
            )

            result: List[EsportsEvent] = await client.get_esports_schedule()

            # Verify correct parsing
            assert isinstance(result, list)
            assert len(result) == len(esports["data"])

            # Verify first event
            first_event = result[0]
            first_mock = esports["data"][0]
            assert isinstance(first_event, EsportsEvent)
            assert type(first_event.date) is datetime

            # Verify league subdataclass
            assert isinstance(first_event.league, EsportsLeague)
            assert first_event.league.name == first_mock["league"]["name"]

            # Verify game type subdataclass
            assert isinstance(first_event.match.game_type, EsportsGameType)
            assert first_event.match.game_type.type == first_mock["match"]["game_type"]["type"]

            # Verify team subdataclass
            first_team = first_event.match.teams[0]
            first_team_mock = first_mock["match"]["teams"][0]
            assert isinstance(first_team, EsportsTeam)
            assert first_team.name == first_team_mock["name"]

            # Verify team record subdataclass
            assert isinstance(first_team.record, EsportsTeamRecord)
            assert first_team.record.wins == first_team_mock["record"]["wins"]

        await client.close()
