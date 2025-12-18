from typing import Any, Dict

import pytest


class TestPremierTeam:
    """Test Premier Team endpoint."""

    @pytest.mark.asyncio
    async def test_premier_team_response_structure(self, premier_team: Dict[str, Any]) -> None:
        """Test that Premier Team response has required structure.

        Parameters
        ----------
        premier_team : Dict[str, Any]
            Mock premier team response data.
        """
        # Verify response structure
        assert "status" in premier_team or "data" in premier_team

    @pytest.mark.asyncio
    async def test_premier_team_has_members(self, premier_team: Dict[str, Any]) -> None:
        """Test that Premier Team has members information.

        Parameters
        ----------
        premier_team : Dict[str, Any]
            Mock premier team response data.
        """
        data = premier_team.get("data", {})

        # If team has members, verify structure
        if "members" in data:
            assert isinstance(data["members"], list)


class TestPremierSearch:
    """Test Premier Search endpoint."""

    @pytest.mark.asyncio
    async def test_premier_search_response_structure(self, premier_search: Dict[str, Any]) -> None:
        """Test that Premier Search response has required structure.

        Parameters
        ----------
        premier_search : Dict[str, Any]
            Mock premier search response data.
        """
        # Verify response structure
        assert "status" in premier_search or "data" in premier_search

    @pytest.mark.asyncio
    async def test_premier_search_returns_teams(self, premier_search: Dict[str, Any]) -> None:
        """Test that Premier Search returns teams list.

        Parameters
        ----------
        premier_search : Dict[str, Any]
            Mock premier search response data.
        """
        data = premier_search.get("data", [])

        if isinstance(data, list):
            # Search results should be a list of teams
            for team in data:
                assert isinstance(team, dict)
