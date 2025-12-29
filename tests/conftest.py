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
    data = MockDataLoader.get("account", "v1")
    return {"status": 200, "data": data}


@pytest.fixture
def account_v2() -> Dict[str, Any]:
    """Get Account V2 mock data."""
    data = MockDataLoader.get("account", "v2")
    return {"status": 200, "data": data}


# Content fixtures
@pytest.fixture
def content() -> Dict[str, Any]:
    """Get Content mock data."""
    data = MockDataLoader.load("content")
    return {"status": 200, "data": data}


# Version fixtures
@pytest.fixture
def version() -> Dict[str, Any]:
    """Get Version mock data."""
    data = MockDataLoader.load("version")
    return {"status": 200, "data": data}


# Website fixtures
@pytest.fixture
def website() -> Dict[str, Any]:
    """Get Website mock data."""
    data = MockDataLoader.get("website", "contents")
    return {"status": 200, "data": data}


# Status fixtures
@pytest.fixture
def status() -> Dict[str, Any]:
    """Get Status mock data."""
    data = MockDataLoader.load("status")
    return {"status": 200, "data": data}


# Queue fixtures
@pytest.fixture
def queue() -> Dict[str, Any]:
    """Get Queue Status mock data."""
    data = MockDataLoader.get("queue", "queues")
    return {"status": 200, "data": data}
