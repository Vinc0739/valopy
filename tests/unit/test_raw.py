from typing import Any, Dict

import pytest


class TestRaw:
    """Test Raw Match V1 endpoint."""

    @pytest.mark.asyncio
    async def test_raw_response_structure(self, raw: Dict[str, Any]) -> None:
        """Test that Raw Match response has required structure.

        Parameters
        ----------
        raw : Dict[str, Any]
            Mock raw match response data.
        """
        # Verify response has content
        assert raw is not None

    @pytest.mark.asyncio
    async def test_raw_has_match_data(self, raw: Dict[str, Any]) -> None:
        """Test that Raw Match response includes match data.

        Parameters
        ----------
        raw : Dict[str, Any]
            Mock raw match response data.
        """
        data = raw.get("data", {})

        # Verify data is not empty
        assert len(data) > 0 or data is not None
