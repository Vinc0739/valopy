from typing import Any, Dict
from unittest.mock import AsyncMock, patch

import pytest

from valopy.client import Client
from valopy.enums import Region
from valopy.models import Result, Status, StatusEntry, StatusUpdate
from valopy.utils import dict_to_dataclass


class TestStatus:
    """Test Status V1 endpoint."""

    @pytest.mark.asyncio
    async def test_get_status_parsing(self, status: Dict[str, Any]) -> None:
        """Test that Status response is correctly parsed.

        Parameters
        ----------
        status : Dict[str, Any]
            Mock status response data.
        """

        client = Client(api_key="test-key")

        status_data = dict_to_dataclass(status["data"], Status)

        with patch.object(client.adapter, "get", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = Result(
                status_code=status["status"], message="OK", data=status_data
            )

            result: Status = await client.get_status(region=Region.EU)

            # Verify correct parsing
            assert isinstance(result, Status)
            assert isinstance(result.maintenances, list)

            # Verify maintenance subdataclass
            maintenance = result.maintenances[0]
            assert isinstance(maintenance, StatusEntry)
            assert maintenance.id == status["data"]["maintenances"][0]["id"]

            # Verify update subdataclass
            assert isinstance(maintenance.updates[0], StatusUpdate)
            assert maintenance.updates[0].author == "Riot Games"

            # Verify title subdataclass
            assert maintenance.titles[0].content is not None

        await client.close()
