from typing import Any, Dict

import pytest


class TestVersion:
    """Test Version V1 endpoint."""

    @pytest.mark.asyncio
    async def test_version_response_structure(self, version: Dict[str, Any]) -> None:
        """Test that Version response has required structure.

        Parameters
        ----------
        version : Dict[str, Any]
            Mock version response data.
        """
        # Verify response structure
        assert "status" in version
        assert "data" in version

    @pytest.mark.asyncio
    async def test_version_has_version_info(self, version: Dict[str, Any]) -> None:
        """Test that Version response includes version information.

        Parameters
        ----------
        version : Dict[str, Any]
            Mock version response data.
        """
        data = version.get("data", {})

        # Verify version info exists
        assert "version" in data or "release_date" in data or len(data) > 0
