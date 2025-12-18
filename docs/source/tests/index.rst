Testing Guide
==============

Valopy includes a comprehensive test suite designed to validate the core functionality of the library's wrapper around the `unofficial Valorant API <https://github.com/Henrik-3/unofficial-valorant-api>`_ created by `Henrik-3 <https://github.com/Henrik-3>`_. This guide explains the test structure and how to run tests.

Test Suite Overview
-------------------

The test suite contains **45 integration tests** organized into **17 test files**, one for each Valorant API endpoint.

**Test Approach:**

ValoPy uses **integration testing** with mocked adapter responses. Each test:

1. Mocks the underlying HTTP adapter (``adapter.get``)
2. Provides realistic JSON responses from test fixtures
3. Calls the ValoPy client method
4. Validates that the client correctly parses and structures the response

This approach tests the actual ValoPy code path, ensuring that responses are properly validated and converted into the appropriate dataclass instances.

Test File Organization
~~~~~~~~~~~~~~~~~~~~~~

Tests are located in the ``tests/unit/`` directory with the following structure:

.. code-block:: text

   tests/
   ├── conftest.py                 # Shared fixtures and configuration
   ├── mock/                       # Mock JSON response data (17 files)
   │   ├── account_v1.json
   │   ├── account_v2.json
   │   ├── content.json
   │   └── ...
   └── unit/
       ├── conftest.py             # Unit test fixtures
       ├── test_account.py          # Account endpoints (4 tests)
       ├── test_content.py          # Content endpoints (2 tests)
       ├── test_crosshair.py        # Crosshair endpoints (2 tests)
       ├── test_esports.py          # Esports endpoints (3 tests)
       ├── test_leaderboard.py      # Leaderboard endpoints (3 tests)
       ├── test_match.py            # Match endpoints (3 tests)
       ├── test_matchlist.py        # Matchlist endpoints (4 tests)
       ├── test_mmr.py              # MMR endpoints (4 tests)
       ├── test_mmr_history.py      # MMR History endpoints (2 tests)
       ├── test_premier.py          # Premier endpoints (4 tests)
       ├── test_queue_status.py     # Queue Status endpoints (2 tests)
       ├── test_raw.py              # Raw endpoints (2 tests)
       ├── test_status.py           # Status endpoints (2 tests)
       ├── test_store.py            # Store endpoints (2 tests)
       ├── test_stored_data.py      # Stored Data endpoints (2 tests)
       ├── test_version.py          # Version endpoints (2 tests)
       └── test_website.py          # Website endpoints (2 tests)

Running Tests
-------------

**Using pytest directly:**

.. code-block:: bash

   pytest tests/unit

**Using pytest with verbose output:**

.. code-block:: bash

   pytest tests/unit -v

**Using pytest with coverage:**

.. code-block:: bash

   pytest tests/unit --cov=valopy

**Using the uv convenience script:**

.. code-block:: bash

   uv run valopy-test

Test Implementation Details
----------------------------

Fixture Architecture
~~~~~~~~~~~~~~~~~~~~

Tests use the ``MockDataLoader`` fixture system for loading mock API responses. Located in ``tests/unit/conftest.py``, this system:

1. **Loads JSON mock data** from ``tests/mock/`` directory
2. **Caches responses** for performance
3. **Provides endpoint-specific fixtures** (e.g., ``account_v1_response``, ``content_response``, etc.)

Each fixture includes realistic API response data that matches the actual Valorant API structure.

Example Test Pattern
~~~~~~~~~~~~~~~~~~~~

A typical ValoPy integration test follows this pattern:

.. code-block:: python

   import pytest
   from unittest.mock import AsyncMock, patch
   from valopy import Client
   from valopy.models import AccountV1

   @pytest.mark.asyncio
   async def test_get_account_v1_parsing(account_v1_response):
       """Test that AccountV1 response is correctly parsed."""
       
       # Setup: Mock the adapter
       with patch("valopy.client.Client._adapter") as mock_adapter:
           mock_adapter.get = AsyncMock(return_value=account_v1_response)
           
           # Execute: Call the client method
           async with Client(api_key="test") as client:
               result = await client.get_account_v1("Player", "TAG")
           
           # Validate: Check the parsed result
           assert isinstance(result, AccountV1)
           assert result.puuid is not None
           assert result.account_level > 0

Test Results
~~~~~~~~~~~~

**Current Status:** ✅ **45 tests passing** (100% success rate)

**Execution Time:** ~0.10s for all 45 tests

**Coverage Areas:**

* Account endpoints (v1, v2)
* Content endpoints with localization
* Player statistics (MMR, leaderboard)
* Match data (v2, v4 APIs)
* Store and inventory data
* Premier and competitive rankings
* Status and utility endpoints

Adding New Tests
----------------

To add tests for new endpoints:

1. **Create mock data**: Add a JSON file to ``tests/mock/`` with realistic response data
2. **Add fixture**: Update ``tests/unit/conftest.py`` with a new endpoint fixture
3. **Create test file**: Add a new ``test_<endpoint>.py`` file in ``tests/unit/``
4. **Implement tests**: Follow the integration test pattern above
5. **Run tests**: Execute ``pytest tests/unit`` to validate

Continuous Integration
----------------------

All tests are designed to run in CI/CD pipelines. They:

* Don't require external API keys
* Don't make real network requests
* Use only mock data from the repository
* Complete in under 1 second
* Produce no side effects

Best Practices
--------------

When working with tests:

* Run tests before committing changes: ``uv run pytest``
* Use descriptive test names: ``test_<method>_<scenario>``
* Test both success and error cases
* Mock external dependencies (HTTP adapter)
* Validate dataclass structure and field types
* Keep tests focused on ValoPy's behavior, not the API itself
