from typing import Any, Dict, List
from unittest.mock import AsyncMock, patch

import pytest

from valopy.client import Client
from valopy.enums import Region
from valopy.models import QueueData, QueueGameRules, QueueMap, QueuePartySize, Result
from valopy.utils import dict_to_dataclass


class TestQueue:
    """Test Queue Status endpoint."""

    @pytest.mark.asyncio
    async def test_get_queue_status_parsing(self, queue: Dict[str, Any]) -> None:
        """Test that Queue Status response is correctly parsed.

        Parameters
        ----------
        queue : Dict[str, Any]
            Mock queue response data.
        """

        client = Client(api_key="test-key")

        queue_data = [dict_to_dataclass(item, QueueData) for item in queue["data"]]

        with patch.object(client.adapter, "get", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = Result(status_code=queue["status"], message="OK", data=queue_data)

            result: List[QueueData] = await client.get_queue_status(region=Region.EU)

            # Verify correct parsing
            assert isinstance(result, list)
            assert len(result) == len(queue["data"])

            # Verify first queue
            first_queue = result[0]
            first_mock = queue["data"][0]
            assert isinstance(first_queue, QueueData)
            assert first_queue.mode == first_mock["mode"]
            assert first_queue.team_size == first_mock["team_size"]

            # Verify party size subdataclass
            assert isinstance(first_queue.party_size, QueuePartySize)
            assert first_queue.party_size.max == first_mock["party_size"]["max"]

            # Verify game rules subdataclass
            assert isinstance(first_queue.game_rules, QueueGameRules)
            assert first_queue.game_rules.premier_mode == first_mock["game_rules"]["premier_mode"]

            # Verify maps subdataclass
            assert isinstance(first_queue.maps, list)
            assert isinstance(first_queue.maps[0], QueueMap)
            assert first_queue.maps[0].map.name == first_mock["maps"][0]["map"]["name"]

        await client.close()
