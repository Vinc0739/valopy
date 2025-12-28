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
            mock_get.return_value = Result(status_code=status["status"], message="OK", data=status_data)

            result: Status = await client.get_status(region=Region.EU)

            # Verify correct parsing
            assert isinstance(result, Status)
            assert isinstance(result.maintenances, list)
            assert isinstance(result.incidents, list)

            # Verify maintenances
            assert len(result.maintenances) == 1
            maintenance = result.maintenances[0]
            assert isinstance(maintenance, StatusEntry)
            assert maintenance.id == status["data"]["maintenances"][0]["id"]
            assert maintenance.maintenance_status == "in_progress"
            assert maintenance.incident_severity == "warning"
            assert "windows" in maintenance.platforms

            # Verify maintenance updates
            assert len(maintenance.updates) == 1
            update = maintenance.updates[0]
            assert isinstance(update, StatusUpdate)
            assert update.author == "Riot Games"
            assert update.publish is True

            # Verify incidents
            assert len(result.incidents) == 1
            incident = result.incidents[0]
            assert isinstance(incident, StatusEntry)
            assert incident.id == status["data"]["incidents"][0]["id"]

        await client.close()
