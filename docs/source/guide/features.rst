Features
========

This page covers ValoPy's core features and how to use them effectively.

Key Features
------------

* 🚀 **Async/Await** - Built on asyncio for non-blocking operations
* 📦 **Auto-parsing** - Automatic JSON parsing into typed dataclass models
* ⏰ **DateTime Parsing** - ISO 8601 datetime strings automatically converted to Python datetime objects
* 🔄 **Error Handling** - Built-in exception classes for API errors
* 📚 **Type Hints** - Full type annotations for IDE support and static analysis

Using the Client
----------------

The :class:`~valopy.client.Client` class is the main entry point for all API interactions.

Context Manager (Recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The recommended way to use the client is as an async context manager, which automatically
handles session cleanup:

.. code-block:: python

   from valopy import Client

   async def main():
       async with Client(api_key="your-api-key") as client:
           account = await client.get_account_v1("Name", "Tag")
           # Session is automatically closed when exiting the block

Manual Session Management
~~~~~~~~~~~~~~~~~~~~~~~~~

For more control, you can manage the session manually:

.. code-block:: python

   from valopy import Client

   async def main():
       client = Client(api_key="your-api-key")
       try:
           account = await client.get_account_v1("Name", "Tag")
       finally:
           await client.close()  # Always close the session

Client Options
~~~~~~~~~~~~~~

The client accepts these parameters:

.. code-block:: python

   client = Client(
       api_key="your-api-key",  # Required: Your API key
       redact_header=True,      # Optional: Redact API key in logs (default: True)
   )

Available Methods
-----------------

The client currently provides these methods:

Account Methods
~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Method
     - Description
   * - :meth:`~valopy.client.Client.get_account_v1`
     - Get account information by name and tag (V1)
   * - :meth:`~valopy.client.Client.get_account_v1_by_puuid`
     - Get account information by PUUID (V1)
   * - :meth:`~valopy.client.Client.get_account_v2`
     - Get account information by name and tag (V2) with additional fields like title and platforms
   * - :meth:`~valopy.client.Client.get_account_v2_by_puuid`
     - Get account information by PUUID (V2) with additional fields like title and platforms

Content Method
~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Method
     - Description
   * - :meth:`~valopy.client.Client.get_content`
     - Get game content including characters, maps, skins, sprays, and acts

Version Method
~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Method
     - Description
   * - :meth:`~valopy.client.Client.get_version`
     - Get current game version information for a specific region

Website Method
~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Method
     - Description
   * - :meth:`~valopy.client.Client.get_website`
     - Get website news articles for a specific country code

Status Methods
~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Method
     - Description
   * - :meth:`~valopy.client.Client.get_status`
     - Get server status including maintenances and incidents for a region

Queue Method
~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Method
     - Description
   * - :meth:`~valopy.client.Client.get_queue_status`
     - Get queue status and configurations for all game modes in a region

Esports Method
~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Method
     - Description
   * - :meth:`~valopy.client.Client.get_esports_schedule`
     - Get esports schedule with optional filtering by region and league

Leaderboard Method
~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Method
     - Description
   * - :meth:`~valopy.client.Client.get_leaderboard`
     - Get leaderboard for a region and platform with optional filtering and pagination

Method Parameters
~~~~~~~~~~~~~~~~~

Most methods support these common parameters:

* ``force_update`` (bool) - Force fresh data instead of cached (default: ``False``)
* ``locale`` (:class:`~valopy.enums.Locale`) - Language/region for localized content
* ``region`` (:class:`~valopy.enums.Region`) - Server region (EU, NA, LATAM, BR, AP, KR)
* ``esports_region`` (:class:`~valopy.enums.EsportsRegion`) - Esports region for filtering events
* ``league`` (:class:`~valopy.enums.League`) - Esports league for filtering events

**Example usage:**

.. code-block:: python

   from valopy import Client, Locale, Region

   async with Client(api_key="your-api-key") as client:
       # Get content in Spanish
       content = await client.get_content(locale=Locale.ES_ES)
       
       # Get version for North America region
       version = await client.get_version(region=Region.NA)
       
       # Force update account data
       account = await client.get_account_v1("Name", "Tag", force_update=True)

For a complete list of all API endpoints (implemented and planned), see :doc:`../endpoints`.

Automatic DateTime Parsing
---------------------------

ValoPy automatically converts datetime strings from the API into Python :class:`datetime.datetime` 
objects. This happens transparently during deserialization, so you get native datetime objects in your models 
without any extra work.

The parser supports multiple datetime formats:

* **ISO 8601** - ``2025-12-04T12:34:56Z`` or ``2025-12-04T12:34:56+00:00``
* **Date-only** - ``2025-12-04``
* **Common format** - ``Dec 4 2025`` (used by some API responses)
* **Relative times** - ``3 minutes ago``, ``2 hours ago``, ``1 day ago``, etc.

Any field that represents a timestamp in the API response is automatically parsed:

.. code-block:: python

   from valopy import Client
   from datetime import datetime, timezone

   async with Client(api_key="your-api-key") as client:
       leaderboard = await client.get_leaderboard(region=Region.NA, platform=Platform.PC)
       
       # updated_at is automatically a datetime object, not a string
       assert isinstance(leaderboard.updated_at, datetime)
       
       # You can use all datetime methods directly
       print(f"Updated: {leaderboard.updated_at.isoformat()}")
       print(f"Days ago: {(datetime.now(timezone.utc) - leaderboard.updated_at).days}")
       
       # Player updates are also parsed
       for player in leaderboard.players:
           print(f"{player.name}: Last updated {player.updated_at.strftime('%Y-%m-%d %H:%M:%S')}")

Fields that support automatic datetime parsing include:

* Account timestamps (``last_update``, ``updated_at``)
* Version information (``build_date``, ``last_checked``)
* Status updates (``created_at``, ``updated_at``, ``archive_at``)
* Esports events (``date``)
* Leaderboard data (``updated_at``)
* Website content (``date``)

Note: Relative time formats (like "3 minutes ago") are converted to UTC datetime representing approximately 
when that time was, relative to the server's current time.

Error Handling
--------------

ValoPy provides specific exception classes for different error scenarios:

.. code-block:: python

   from valopy import (
       Client,
       ValoPyNotFoundError,
       ValoPyPermissionError,
       ValoPyRateLimitError,
   )

   async with Client(api_key="your-api-key") as client:
       try:
           account = await client.get_account_v1("Name", "Tag")
       except ValoPyNotFoundError:
           print("Account not found")
       except ValoPyPermissionError:
           print("Invalid API key")
       except ValoPyRateLimitError as e:
           print(f"Rate limited, retry after {e.rate_reset}s")

See :doc:`../api/exceptions` for the complete exception hierarchy.

Caching
-------

ValoPy includes built-in caching support to reduce API calls and improve performance. By default,
caching is enabled with a 1-hour TTL (time-to-live) for all responses.

Basic Usage
~~~~~~~~~~~

Caching is enabled by default:

.. code-block:: python

   from valopy import Client

   async with Client(api_key="your-api-key") as client:
       # First call: Makes API request and caches response
       account1 = await client.get_account_v1("Name", "Tag")
       
       # Second call: Returns cached response (no API call)
       account2 = await client.get_account_v1("Name", "Tag")

Disabling Caching
~~~~~~~~~~~~~~~~~

To disable caching entirely:

.. code-block:: python

   from valopy import Client

   async with Client(api_key="your-api-key", caching=False) as client:
       # All calls make fresh API requests
       account = await client.get_account_v1("Name", "Tag")

Custom Cache Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure cache behavior globally and per-endpoint:

.. code-block:: python

   from valopy import Client, CacheConfig, EndpointCacheConfig, Endpoint

   # Create custom cache config
   cache_config = CacheConfig(
       enabled=True,
       default_ttl=3600,  # 1 hour default
       endpoints={
           Endpoint.ACCOUNT_BY_NAME_V1: EndpointCacheConfig(
               enabled=True,
               ttl=1800  # 30 minutes for this specific endpoint
           ),
           Endpoint.STATUS: EndpointCacheConfig(
               enabled=False  # Disable caching for status endpoint
           ),
       }
   )

   async with Client(api_key="your-api-key", caching=cache_config) as client:
       account = await client.get_account_v1("Name", "Tag")
       status = await client.get_status(region=Region.NA)

Cache Management
~~~~~~~~~~~~~~~~

Manage the cache programmatically:

.. code-block:: python

   from valopy import Client

   async with Client(api_key="your-api-key") as client:
       account = await client.get_account_v1("Name", "Tag")
       
       # Get cache statistics
       stats = client.get_cache_stats()
       print(f"Active entries: {stats['active_entries']}")
       print(f"Total entries: {stats['total_entries']}")
       
       # Clear all cached entries
       client.clear_cache()
       
       # Remove only expired entries
       client.clear_expired_cache()

Cache Key Generation
~~~~~~~~~~~~~~~~~~~~~

Cache keys are generated based on:

1. **Endpoint path** - The formatted URL with parameters (e.g., ``/account-v1/Name/Tag``)
2. **Query parameters** - Any query parameters passed (e.g., ``force=false``)

This ensures that different requests produce different cache entries. For example:

.. code-block:: python

   async with Client(api_key="your-api-key") as client:
       # These produce different cache entries (different account names)
       account1 = await client.get_account_v1("Name1", "Tag1")
       account2 = await client.get_account_v1("Name2", "Tag2")
       
       # These use the same cache entry
       account1_cached = await client.get_account_v1("Name1", "Tag1")

Force Updates (API Parameter)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``force_update`` parameter is an API-level parameter, not a cache-bypass mechanism:

.. code-block:: python

   from valopy import Client

   async with Client(api_key="your-api-key") as client:
       # First call with force_update=False
       account = await client.get_account_v1("Name", "Tag", force_update=False)
       
       # Second call with force_update=True - uses DIFFERENT cache entry
       account = await client.get_account_v1("Name", "Tag", force_update=True)

**Important:** The ``force_update`` parameter tells the API to refresh data on their side, but the response 
is still cached by ValoPy. Each combination of parameters creates a separate cache entry. For example:

* ``get_account_v1("Name", "Tag", force_update=False)`` - cached separately
* ``get_account_v1("Name", "Tag", force_update=True)`` - cached separately
* These two calls produce different cache entries even though they fetch the same account

To truly bypass caching, configure it at initialization time:

.. code-block:: python

   from valopy import Client, CacheConfig, EndpointCacheConfig, Endpoint

   # Option 1: Disable caching for specific endpoints
   cache_config = CacheConfig(
       endpoints={
           Endpoint.ACCOUNT_BY_NAME_V1: EndpointCacheConfig(enabled=False)
       }
   )
   async with Client(api_key="your-api-key", caching=cache_config) as client:
       account = await client.get_account_v1("Name", "Tag")  # Not cached
       
   # Option 2: Disable caching completely
   async with Client(api_key="your-api-key", caching=False) as client:
       account = await client.get_account_v1("Name", "Tag")  # No caching at all

Notes on Caching
~~~~~~~~~~~~~~~~

* Cache is in-memory only (not persistent between sessions)
* Expired entries are automatically removed when accessed
* Cache is cleared when the client is closed
* Using :meth:`~valopy.client.Client.clear_expired_cache` periodically can help manage memory
* The ``force_update`` parameter is API-level only and does NOT bypass the cache; different parameter combinations create separate cache entries