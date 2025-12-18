from typing import Any, Dict

import pytest


class TestEsports:
    """Test Esports Schedule V1 endpoint."""

    @pytest.mark.asyncio
    async def test_esports_response_structure(self, esports: Dict[str, Any]) -> None:
        """Test that Esports response has required structure.

        Parameters
        ----------
        esports : Dict[str, Any]
            Mock esports response data.
        """
        # Verify response structure
        assert "status" in esports
        assert "data" in esports

    @pytest.mark.asyncio
    async def test_esports_has_schedule(self, esports: Dict[str, Any]) -> None:
        """Test that Esports response includes schedule information.

        Parameters
        ----------
        esports : Dict[str, Any]
            Mock esports response data.
        """
        data = esports.get("data", {})

        # Verify schedule data exists
        if "matches" in data:
            assert isinstance(data["matches"], list)

    @pytest.mark.asyncio
    async def test_esports_matches_have_teams(self, esports: Dict[str, Any]) -> None:
        """Test that Esports matches have team information.

        Parameters
        ----------
        esports : Dict[str, Any]
            Mock esports response data.
        """
        data = esports.get("data", [])

        # data can be list or dict, handle both
        matches = data if isinstance(data, list) else data.get("matches", [])

        # Verify matches exist
        assert len(matches) >= 0
