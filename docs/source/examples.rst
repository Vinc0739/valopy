Examples
========

This page contains practical examples for common use cases.

.. contents:: On this page
   :local:
   :depth: 2

Account Information
-------------------

Basic Account Lookup (V1)
~~~~~~~~~~~~~~~~~~~~~~~~~

Fetch basic account information using the V1 endpoint:

.. code-block:: python

   import asyncio
   from valopy import Client

   async def get_account_info():
       async with Client(api_key="your-api-key") as client:
           account = await client.get_account_v1("PlayerName", "TAG")

           print(f"Player: {account.name}#{account.tag}")
           print(f"PUUID: {account.puuid}")
           print(f"Region: {account.region}")
           print(f"Level: {account.account_level}")
           print(f"Last Update: {account.last_update}")

           # Access card information
           print(f"Card ID: {account.card.id}")
           print(f"Card (Small): {account.card.small}")
           print(f"Card (Large): {account.card.large}")
           print(f"Card (Wide): {account.card.wide}")

   asyncio.run(get_account_info())

Account Lookup (V2)
~~~~~~~~~~~~~~~~~~~

The V2 endpoint provides additional information like title and platforms:

.. code-block:: python

   import asyncio
   from valopy import Client

   async def get_account_v2_info():
       async with Client(api_key="your-api-key") as client:
           account = await client.get_account_v2("PlayerName", "TAG")

           print(f"Player: {account.name}#{account.tag}")
           print(f"PUUID: {account.puuid}")
           print(f"Region: {account.region}")
           print(f"Level: {account.account_level}")
           print(f"Title: {account.title}")
           print(f"Card ID: {account.card}")
           print(f"Platforms: {', '.join(account.platforms)}")
           print(f"Updated At: {account.updated_at}")

   asyncio.run(get_account_v2_info())

Force Update
~~~~~~~~~~~~

Force the API to fetch fresh data instead of cached:

.. code-block:: python

   import asyncio
   from valopy import Client

   async def force_update_account():
       async with Client(api_key="your-api-key") as client:
           # Force update the account data
           account = await client.get_account_v1("PlayerName", "TAG", force_update=True)

           print(f"Fresh data for: {account.name}#{account.tag}")
           print(f"Updated at: {account.last_update}")

   asyncio.run(force_update_account())

Game Content
------------

Fetching Content
~~~~~~~~~~~~~~~~

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
           print(f"Skins: {len(content.skins)}")
           print(f"Acts: {len(content.acts)}")

           # List all characters
           print("\nAvailable Characters:")
           for character in content.characters:
               print(f"  - {character.name} (ID: {character.id})")

           # List active acts
           print("\nActive Acts:")
           for act in content.acts:
               if act.isActive:
                   print(f"  - {act.name} (ID: {act.id})")

   asyncio.run(get_content())

Searching Content
~~~~~~~~~~~~~~~~~

Search for specific content items:

.. code-block:: python

   import asyncio
   from valopy import Client

   async def search_content():
       async with Client(api_key="your-api-key") as client:
           content = await client.get_content()

           # Find a specific character by name
           jett = next((char for char in content.characters if char.name == "Jett"), None)

           if jett:
               print(f"Found: {jett.name}")
               print(f"  ID: {jett.id}")
               print(f"  Asset: {jett.assetName}")

           # Find all active acts
           active_acts = [act for act in content.acts if act.isActive]
           print(f"\nActive Acts: {len(active_acts)}")
           for act in active_acts:
               print(f"  - {act.name}")

           # Get all skins
           print(f"\nTotal Skins: {len(content.skins)}")

   asyncio.run(search_content())

Localized Content
~~~~~~~~~~~~~~~~~

Fetch content in different languages using the ``Locale`` enum:

.. note::

   The ``localizedNames`` property for content objects is currently always ``None``, but see 
   this as a placeholder example which shows how you would access them once the API provides this data.

.. code-block:: python

   import asyncio
   from valopy import Client, Locale

   async def get_localized_content():
       async with Client(api_key="your-api-key") as client:
           # Get content in Spanish
           content = await client.get_content(locale=Locale.ES_ES)

           print("Characters (Spanish):")
           for character in content.characters[:5]:
               print(f"  - {character.name}")

           # Get content in Japanese
           content_jp = await client.get_content(locale=Locale.JA_JP)

           print("\nCharacters (Japanese):")
           for character in content_jp.characters[:5]:
               print(f"  - {character.name}")

   asyncio.run(get_localized_content())

Localized Names
~~~~~~~~~~~~~~~

Access localized names for content:

.. note::

   The ``localizedNames`` property for content objects is currently always ``None``, but see 
   this as a placeholder example which shows how you would access them once the API provides this data.

.. code-block:: python

   import asyncio
   from valopy import Client, Locale

   async def display_localized_names():
       async with Client(api_key="your-api-key") as client:
           content = await client.get_content(locale=Locale.EN_US)

           # Display character with localized names
           for character in content.characters[:3]:
               print(f"\nCharacter: {character.name}")
               if character.localizedNames:
                   print("  Localized names:")
                   # Show a few locales
                   for locale in ["en-US", "es-ES", "ja-JP"]:
                       if locale in character.localizedNames:
                           print(f"    {locale}: {character.localizedNames[locale]}")

   asyncio.run(display_localized_names())

Error Handling
--------------

Basic Error Handling
~~~~~~~~~~~~~~~~~~~~

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
               print(f"Rate limit exceeded: {e.rate_remain}/{e.rate_limit}")
               print(f"Retry after: {e.rate_reset} seconds")

           except ValoPyHTTPError as e:
               print(f"HTTP Error {e.status_code}: {e.message}")

   asyncio.run(safe_fetch_account())

Retry with Exponential Backoff
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implement retry logic for rate limits:

.. code-block:: python

   import asyncio
   from valopy import Client, ValoPyHTTPError, ValoPyRateLimitError

   async def fetch_with_retry(client, max_retries=3):
       """Fetch account with retry logic."""
       retry_count = 0
       base_delay = 1

       while retry_count < max_retries:
           try:
               account = await client.get_account_v1("PlayerName", "TAG")
               return account

           except ValoPyRateLimitError:
               retry_count += 1
               if retry_count >= max_retries:
                   print("Max retries reached")
                   raise

               delay = base_delay * (2 ** retry_count)
               print(f"Rate limited. Retrying in {delay}s...")
               await asyncio.sleep(delay)

           except ValoPyHTTPError as e:
               print(f"HTTP Error: {e.status_code} - {e.message}")
               raise

   async def main():
       async with Client(api_key="your-api-key") as client:
           try:
               account = await fetch_with_retry(client)
               print(f"Success: {account.name}#{account.tag}")
           except Exception as e:
               print(f"Failed: {e}")

   asyncio.run(main())

Concurrent Requests
-------------------

Batch Requests
~~~~~~~~~~~~~~

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
           # Fetch all accounts concurrently
           tasks = [client.get_account_v1(name, tag) for name, tag in players]
           accounts = await asyncio.gather(*tasks, return_exceptions=True)

           # Process results
           for (name, tag), result in zip(players, accounts):
               if isinstance(result, Exception):
                   print(f"{name}#{tag}: Error - {result}")
               else:
                   print(f"{name}#{tag}: Level {result.account_level}")

   asyncio.run(fetch_multiple_accounts())

.. note::

   When using ``return_exceptions=True``, failed requests return exception objects
   instead of raising them, allowing you to handle errors per-request.
