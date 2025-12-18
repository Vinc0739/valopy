from typing import Any, Dict

import pytest


class TestMatchlistV3:
    """Test Matchlist V3 endpoint."""

    @pytest.mark.asyncio
    async def test_matchlist_v3_response_structure(self, matchlist_v3: Dict[str, Any]) -> None:
        """Test that Matchlist V3 response has required structure.

        Parameters
        ----------
        matchlist_v3 : Dict[str, Any]
            Mock matchlist V3 response data.
        """
        # Verify response structure
        assert "status" in matchlist_v3
        assert matchlist_v3["status"] == 200
        assert "data" in matchlist_v3

    @pytest.mark.asyncio
    async def test_matchlist_v3_data_is_list(self, matchlist_v3: Dict[str, Any]) -> None:
        """Test that Matchlist V3 data is a list of match IDs.

        Parameters
        ----------
        matchlist_v3 : Dict[str, Any]
            Mock matchlist V3 response data.
        """
        data = matchlist_v3.get("data", [])
        assert isinstance(data, list)


class TestMatchlistV4:
    """Test Matchlist V4 endpoint."""

    @pytest.mark.asyncio
    async def test_matchlist_v4_response_structure(self, matchlist_v4: Dict[str, Any]) -> None:
        """Test that Matchlist V4 response has required structure.

        Parameters
        ----------
        matchlist_v4 : Dict[str, Any]
            Mock matchlist V4 response data.
        """
        # Verify response structure
        assert "status" in matchlist_v4
        assert matchlist_v4["status"] == 200
        assert "data" in matchlist_v4

    @pytest.mark.asyncio
    async def test_matchlist_v4_data_is_list(self, matchlist_v4: Dict[str, Any]) -> None:
        """Test that Matchlist V4 data is a list of match entries.

        Parameters
        ----------
        matchlist_v4 : Dict[str, Any]
            Mock matchlist V4 response data.
        """
        data = matchlist_v4.get("data", [])
        assert isinstance(data, list)
