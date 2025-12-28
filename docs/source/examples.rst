Examples
========

This page contains practical examples for common use cases.

.. contents:: On this page
   :local:
   :depth: 2

Account Information
-------------------

Basic Account Lookup
~~~~~~~~~~~~~~~~~~~~

Fetch account information using the V1 or V2 endpoints:

.. code-block:: python

   import asyncio
   from valopy import Client

   async def get_account_info():
       async with Client(api_key="your-api-key") as client:
           # V1 endpoint - includes card images
           account = await client.get_account_v1("PlayerName", "TAG")

           print(f"Player: {account.name}#{account.tag}")
           print(f"PUUID: {account.puuid}")
           print(f"Region: {account.region}")
           print(f"Level: {account.account_level}")
           print(f"Card (Large): {account.card.large}")

           # V2 endpoint - includes title and platforms
           account_v2 = await client.get_account_v2("PlayerName", "TAG")

           print(f"Title: {account_v2.title}")
           print(f"Platforms: {', '.join(account_v2.platforms)}")

   asyncio.run(get_account_info())

Lookup by PUUID
~~~~~~~~~~~~~~~

Fetch account information using a player's PUUID:

.. code-block:: python

   import asyncio
   from valopy import Client

   async def get_account_by_puuid():
       async with Client(api_key="your-api-key") as client:
           account = await client.get_account_v1_by_puuid("player-puuid-here")
           
           print(f"Player: {account.name}#{account.tag}")
           print(f"Level: {account.account_level}")

   asyncio.run(get_account_by_puuid())

Game Content
------------

Get game content like characters, maps, and skins:

.. code-block:: python

   import asyncio
   from valopy import Client

   async def get_content():
       async with Client(api_key="your-api-key") as client:
           content = await client.get_content()

           print(f"Version: {content.version}")
           print(f"Characters: {len(content.characters)}")
           print(f"Maps: {len(content.maps)}")

           # List all characters
           for character in content.characters:
               print(f"  - {character.name}")

   asyncio.run(get_content())

Website News
------------

Get website news for a specific country:

.. code-block:: python

   import asyncio
   from valopy import Client, CountryCode

   async def get_news():
       async with Client(api_key="your-api-key") as client:
           articles = await client.get_website(countrycode=CountryCode.EN_US)

           for article in articles[:5]:  # Show first 5 articles
               print(f"Title: {article.title}")
               print(f"Category: {article.category}")
               print(f"Date: {article.date}")
               print(f"URL: {article.url}")
               print()

   asyncio.run(get_news())

Server Status
-------------

Get current server status and maintenance announcements:

.. code-block:: python

   import asyncio
   from valopy import Client, Region

   async def get_server_status():
       async with Client(api_key="your-api-key") as client:
           status = await client.get_status(region=Region.EU)

           # Check if there are any maintenances or incidents
           if not status.maintenances and not status.incidents:
               print("No maintenances or incidents reported!")
               return

           # Show latest maintenance if any
           if status.maintenances:
               maintenance = status.maintenances[0]
               print(f"Maintenance: {maintenance.maintenance_status}")
               if maintenance.titles:
                   print(f"  Title: {maintenance.titles[0].content}")

           # Show latest incident if any
           if status.incidents:
               incident = status.incidents[0]
               if incident.updates and incident.updates[0].translations:
                   print(f"Incident: {incident.updates[0].translations[0].content}")

   asyncio.run(get_server_status())

Error Handling
--------------

Handle common API errors:

.. code-block:: python

   import asyncio
   from valopy import (
       Client,
       ValoPyNotFoundError,
       ValoPyPermissionError,
       ValoPyRateLimitError,
       ValoPyHTTPError,
   )

   async def safe_fetch_account():
       async with Client(api_key="your-api-key") as client:
           try:
               account = await client.get_account_v1("PlayerName", "TAG")
               print(f"Found: {account.name}#{account.tag}")

           except ValoPyNotFoundError:
               print("Account not found!")

           except ValoPyPermissionError:
               print("Invalid API key or insufficient permissions")

           except ValoPyRateLimitError as e:
               print(f"Rate limit exceeded. Retry after: {e.rate_reset} seconds")

           except ValoPyHTTPError as e:
               print(f"HTTP Error {e.status_code}: {e.message}")

   asyncio.run(safe_fetch_account())

Concurrent Requests
-------------------

Fetch multiple accounts concurrently using ``asyncio.gather``:

.. code-block:: python

   import asyncio
   from valopy import Client

   async def fetch_multiple_accounts():
       players = [
           ("Player1", "TAG1"),
           ("Player2", "TAG2"),
           ("Player3", "TAG3"),
       ]

       async with Client(api_key="your-api-key") as client:
           tasks = [client.get_account_v1(name, tag) for name, tag in players]
           accounts = await asyncio.gather(*tasks, return_exceptions=True)

           for (name, tag), result in zip(players, accounts):
               if isinstance(result, Exception):
                   print(f"{name}#{tag}: Error - {result}")
               else:
                   print(f"{name}#{tag}: Level {result.account_level}")

   asyncio.run(fetch_multiple_accounts())

.. note::

   When using ``return_exceptions=True``, failed requests return exception objects
   instead of raising them, allowing you to handle errors per-request.
