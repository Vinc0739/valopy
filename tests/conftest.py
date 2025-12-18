"""Shared test utilities for unit tests."""

import json
from pathlib import Path
from typing import Any, Dict
from unittest.mock import AsyncMock

import pytest

from valopy.models import Result


@pytest.fixture
def mock_result() -> Result:
    """Create a mock Result object."""
    return Result(status_code=200, message="OK", data={})


@pytest.fixture
def adapter_mock():
    """Create a mock adapter for testing.

    Returns an async mock that can be used to patch adapter._do method.
    """
    return AsyncMock()


@pytest.fixture
def mock_adapter_get_result():
    """Factory fixture for creating mock adapter get results.

    Returns a function that creates Result objects with specified data.
    """
    def _create_result(data: Dict[str, Any]) -> Result:
        return Result(status_code=200, message="OK", data=data)
    return _create_result


# Import MockDataLoader from parent conftest
class MockDataLoader:
    """Load mock API response data from JSON files.

    Caches loaded JSON data from mock files to improve test performance.
    """

    _cache: Dict[str, Any] = {}

    @classmethod
    def load(cls, endpoint: str) -> Dict[str, Any]:
        """Load mock data from JSON file.

        Parameters
        ----------
        endpoint : str
            The endpoint name (e.g., 'account', 'match').

        Returns
        -------
        Dict[str, Any]
            The loaded mock data.
        """
        if endpoint not in cls._cache:
            mock_path = Path(__file__).parent / "mock" / f"{endpoint}.json"
            with open(mock_path) as f:
                cls._cache[endpoint] = json.load(f)
        return cls._cache[endpoint]

    @classmethod
    def get(cls, endpoint: str, key: str) -> Any:
        """Get specific mock data by endpoint and key.

        Parameters
        ----------
        endpoint : str
            The endpoint name.
        key : str
            The data key within the mock file.

        Returns
        -------
        Any
            The requested mock data.
        """
        return cls.load(endpoint).get(key)


# Account fixtures
@pytest.fixture
def account_v1() -> Dict[str, Any]:
    """Get Account V1 mock data."""
    return MockDataLoader.get("account", "v1_by_name_tag")


@pytest.fixture
def account_v2() -> Dict[str, Any]:
    """Get Account V2 mock data."""
    return MockDataLoader.get("account", "v2_by_name_tag")


# Content fixtures
@pytest.fixture
def content() -> Dict[str, Any]:
    """Get Content mock data."""
    data = MockDataLoader.load("content")
    return data if data.get("status") else {"status": 200, "data": data}


# Crosshair fixtures
@pytest.fixture
def crosshair() -> Dict[str, Any]:
    """Get Crosshair mock data."""
    data = MockDataLoader.load("crosshair")
    return data if data.get("status") else {"status": 200, "data": data}


# Esports fixtures
@pytest.fixture
def esports() -> Dict[str, Any]:
    """Get Esports mock data."""
    data = MockDataLoader.get("esports", "esports_schedule")
    return data if data else MockDataLoader.load("esports")


# Leaderboard fixtures
@pytest.fixture
def leaderboard() -> Dict[str, Any]:
    """Get Leaderboard mock data."""
    data = MockDataLoader.get("leaderboard", "v3_leaderboard")
    return data if data else MockDataLoader.load("leaderboard")


# Match fixtures
@pytest.fixture
def match_v2() -> Dict[str, Any]:
    """Get Match V2 mock data."""
    data = MockDataLoader.get("match", "v2_match_details")
    return data if data else MockDataLoader.load("match")


@pytest.fixture
def match_v4() -> Dict[str, Any]:
    """Get Match V4 mock data."""
    data = MockDataLoader.get("match", "v4_match_details")
    return data if data else MockDataLoader.load("match")


# Matchlist fixtures
@pytest.fixture
def matchlist_v3() -> Dict[str, Any]:
    """Get Matchlist V3 mock data."""
    data = MockDataLoader.get("matchlist", "v3_matches")
    return data if data else MockDataLoader.load("matchlist")


@pytest.fixture
def matchlist_v4() -> Dict[str, Any]:
    """Get Matchlist V4 mock data."""
    data = MockDataLoader.get("matchlist", "v4_matches")
    return data if data else MockDataLoader.load("matchlist")


# MMR fixtures
@pytest.fixture
def mmr_v2() -> Dict[str, Any]:
    """Get MMR V2 mock data."""
    data = MockDataLoader.get("mmr", "v2_mmr")
    return data if data else MockDataLoader.load("mmr")


@pytest.fixture
def mmr_v3() -> Dict[str, Any]:
    """Get MMR V3 mock data."""
    data = MockDataLoader.get("mmr", "v3_mmr")
    return data if data else MockDataLoader.load("mmr")


# MMR History fixtures
@pytest.fixture
def mmr_history() -> Dict[str, Any]:
    """Get MMR History mock data."""
    data = MockDataLoader.load("mmr_history")
    return data if data else {}


# Premier fixtures
@pytest.fixture
def premier_team() -> Dict[str, Any]:
    """Get Premier Team mock data."""
    data = MockDataLoader.get("premier", "team_details")
    return data if data else MockDataLoader.load("premier")


@pytest.fixture
def premier_search() -> Dict[str, Any]:
    """Get Premier Search mock data."""
    data = MockDataLoader.get("premier", "team_search")
    return data if data else MockDataLoader.load("premier")


# Queue Status fixtures
@pytest.fixture
def queue_status() -> Dict[str, Any]:
    """Get Queue Status mock data."""
    data = MockDataLoader.get("queue_status", "queue_status")
    return data if data else MockDataLoader.load("queue_status")


# Raw fixtures
@pytest.fixture
def raw() -> Dict[str, Any]:
    """Get Raw match mock data."""
    data = MockDataLoader.load("raw")
    return data if data else {}


# Status fixtures
@pytest.fixture
def status() -> Dict[str, Any]:
    """Get Status mock data."""
    data = MockDataLoader.get("status", "status_response")
    return data if data else MockDataLoader.load("status")


# Stored Data fixtures
@pytest.fixture
def stored_data() -> Dict[str, Any]:
    """Get Stored Data mock data."""
    data = MockDataLoader.load("stored_data")
    return data if data else {}


# Store fixtures
@pytest.fixture
def store() -> Dict[str, Any]:
    """Get Store mock data."""
    data = MockDataLoader.load("store")
    return data if data else {}


# Version fixtures
@pytest.fixture
def version() -> Dict[str, Any]:
    """Get Version mock data."""
    data = MockDataLoader.get("version", "version_response")
    return data if data else MockDataLoader.load("version")


# Website fixtures
@pytest.fixture
def website() -> Dict[str, Any]:
    """Get Website mock data."""
    data = MockDataLoader.load("website")
    return data if data else {}
