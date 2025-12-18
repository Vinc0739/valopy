Working with Accounts
=====================

This guide covers how to fetch and work with Valorant account information.

Account V1 Endpoint
-------------------

The V1 endpoint provides basic account information including card images.

Basic Account Fetch
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import asyncio
   from valopy import Client

   async def get_account_info():
       async with Client(api_key="your-api-key") as client:
           # Fetch account information
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

Account V2 Endpoint
-------------------

The V2 endpoint provides additional information like platforms and titles.

Fetching Account V2 Data
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import asyncio
   from valopy import Client

   async def get_account_v2_info():
       async with Client(api_key="your-api-key") as client:
           # Fetch account information (V2)
           account = await client.get_account_v2("PlayerName", "TAG")
           
           print(f"Player: {account.name}#{account.tag}")
           print(f"PUUID: {account.puuid}")
           print(f"Region: {account.region}")
           print(f"Level: {account.account_level}")
           print(f"Title: {account.title}")
           print(f"Card ID: {account.card_id}")
           print(f"Platforms: {', '.join(account.platforms)}")
           print(f"Updated At: {account.updated_at}")

   asyncio.run(get_account_v2_info())

Force Update
------------

Force Update Account Data
~~~~~~~~~~~~~~~~~~~~~~~~~

Force the API to update cached account information:

.. code-block:: python

   import asyncio
   from valopy import Client

   async def force_update_account():
       async with Client(api_key="your-api-key") as client:
           # Force update the account data
           account = await client.get_account_v1(
               "PlayerName", 
               "TAG",
               force_update=True
           )
           
           print(f"Fresh data for: {account.name}#{account.tag}")
           print(f"Updated at: {account.last_update}")

   asyncio.run(force_update_account())

Batch Account Fetching
----------------------

Fetch Multiple Accounts Concurrently
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
           tasks = [
               client.get_account_v1(name, tag)
               for name, tag in players
           ]
           
           accounts = await asyncio.gather(*tasks, return_exceptions=True)
           
           # Process results
           for (name, tag), result in zip(players, accounts):
               if isinstance(result, Exception):
                   print(f"{name}#{tag}: Error - {result}")
               else:
                   print(f"{name}#{tag}: Level {result.account_level}")

   asyncio.run(fetch_multiple_accounts())
