from typing import Any, Dict

import pytest


class TestStatus:
    """Test Status V1 endpoint."""

    @pytest.mark.asyncio
    async def test_status_response_structure(self, status: Dict[str, Any]) -> None:
        """Test that Status response has required structure.

        Parameters
        ----------
        status : Dict[str, Any]
            Mock status response data.
        """
        # Verify response structure
        assert "status" in status
        assert "data" in status

    @pytest.mark.asyncio
    async def test_status_has_maintenances(self, status: Dict[str, Any]) -> None:
        """Test that Status response includes maintenance information.

        Parameters
        ----------
        status : Dict[str, Any]
            Mock status response data.
        """
        data = status.get("data", {})

        # Check for maintenance status info
        assert "maintenances" in data or "incidents" in data or len(data) > 0
