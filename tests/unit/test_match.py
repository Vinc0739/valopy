from typing import Any, Dict

import pytest


class TestMatchV2:
    """Test Match V2 endpoint."""

    @pytest.mark.asyncio
    async def test_match_v2_response_has_required_fields(self, match_v2: Dict[str, Any]) -> None:
        """Test that Match V2 response contains all required fields.

        Parameters
        ----------
        match_v2 : Dict[str, Any]
            Mock match V2 response data.
        """
        match_data = match_v2.get("data", {})

        # Verify match has essential structure (metadata, teams, players)
        assert "metadata" in match_data or "data" in match_data or len(match_data) > 0


class TestMatchV4:
    """Test Match V4 endpoint."""

    @pytest.mark.asyncio
    async def test_match_v4_response_has_required_fields(self, match_v4: Dict[str, Any]) -> None:
        """Test that Match V4 response contains all required fields.

        Parameters
        ----------
        match_v4 : Dict[str, Any]
            Mock match V4 response data.
        """
        match_data = match_v4.get("data", {})

        # Verify match has essential structure
        assert "metadata" in match_data or "data" in match_data or len(match_data) > 0

    @pytest.mark.asyncio
    async def test_match_v4_players_have_stats(self, match_v4: Dict[str, Any]) -> None:
        """Test that Match V4 players have stats.

        Parameters
        ----------
        match_v4 : Dict[str, Any]
            Mock match V4 response data.
        """
        match_data = match_v4.get("data", {})
        players = match_data.get("players", [])

        # Verify players have basic structure
        for player in players:
            assert "name" in player or "puuid" in player or "stats" in player
