from typing import Any, Dict

import pytest


class TestQueueStatus:
    """Test Queue Status V1 endpoint."""

    @pytest.mark.asyncio
    async def test_queue_status_response_structure(self, queue_status: Dict[str, Any]) -> None:
        """Test that Queue Status response has required structure.

        Parameters
        ----------
        queue_status : Dict[str, Any]
            Mock queue status response data.
        """
        # Verify response structure
        assert "status" in queue_status
        assert "data" in queue_status

    @pytest.mark.asyncio
    async def test_queue_status_has_queue_info(self, queue_status: Dict[str, Any]) -> None:
        """Test that Queue Status includes queue information.

        Parameters
        ----------
        queue_status : Dict[str, Any]
            Mock queue status response data.
        """
        data = queue_status.get("data", {})

        # Verify queue info exists
        assert len(data) > 0 or "queues" in data
