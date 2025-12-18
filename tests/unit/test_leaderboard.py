from typing import Any, Dict

import pytest


class TestLeaderboard:
    """Test Leaderboard V3 endpoint."""

    @pytest.mark.asyncio
    async def test_leaderboard_response_structure(self, leaderboard: Dict[str, Any]) -> None:
        """Test that Leaderboard response has required structure.

        Parameters
        ----------
        leaderboard : Dict[str, Any]
            Mock leaderboard response data.
        """
        # Verify response structure
        assert "status" in leaderboard
        assert "data" in leaderboard

    @pytest.mark.asyncio
    async def test_leaderboard_ranking_consistency(self, leaderboard: Dict[str, Any]) -> None:
        """Test that leaderboard rankings are in ascending order.

        Parameters
        ----------
        leaderboard : Dict[str, Any]
            Mock leaderboard response data.
        """
        data = leaderboard.get("data", {})
        players = data.get("players", [])

        # Verify ranks are in order
        if len(players) > 1:
            for i in range(len(players) - 1):
                current_rank = players[i].get("rank", 0)
                next_rank = players[i + 1].get("rank", 0)
                # Each subsequent player should have equal or higher rank number
                assert current_rank <= next_rank

    @pytest.mark.asyncio
    async def test_leaderboard_player_data(self, leaderboard: Dict[str, Any]) -> None:
        """Test that leaderboard players have required fields.

        Parameters
        ----------
        leaderboard : Dict[str, Any]
            Mock leaderboard response data.
        """
        data = leaderboard.get("data", {})
        players = data.get("players", [])

        if players:
            for player in players:
                # Players should have name, tag, or leaderboard_rank
                assert "name" in player or "leaderboard_rank" in player
