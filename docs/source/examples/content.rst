Working with Content
====================

This guide covers how to fetch and work with Valorant game content like agents, maps, and skins.

Fetching Game Content
---------------------

Basic Content Fetch
~~~~~~~~~~~~~~~~~~~

Retrieve information about in-game content like agents, maps, skins, and more:

.. code-block:: python

   import asyncio
   from valopy import Client

   async def get_content():
       async with Client(api_key="your-api-key") as client:
           # Get content data
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
           
           # List active acts - Note: acts have an isActive property
           print("\nActive Acts:")
           for act in content.acts:
               if act.isActive:
                   print(f"  - {act.name} (ID: {act.id})")

   asyncio.run(get_content())

Localized Content
-----------------

Fetching Content with Locale
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get content in a specific language:

.. code-block:: python

   import asyncio
   from valopy import Client, Locals

   async def get_localized_content():
       async with Client(api_key="your-api-key") as client:
           # Get content in Spanish
           content = await client.get_content(locale=Locals.ES_ES)
           
           print("Characters (Spanish):")
           for character in content.characters[:5]:  # First 5
               print(f"  - {character.name}")
               # Access localized names if available
               if character.localizedNames and 'es-ES' in character.localizedNames:
                   print(f"    Spanish: {character.localizedNames['es-ES']}")
           
           # Get content in Japanese
           content_jp = await client.get_content(locale=Locals.JA_JP)
           
           print("\nCharacters (Japanese):")
           for character in content_jp.characters[:5]:  # First 5
               print(f"  - {character.name}")

   asyncio.run(get_localized_content())

Searching Content
-----------------

Filter and Search Content Items
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import asyncio
   from valopy import Client

   async def search_content():
       async with Client(api_key="your-api-key") as client:
           content = await client.get_content()
           
           # Find a specific character by name
           jett = next(
               (char for char in content.characters if char.name == "Jett"),
               None
           )
           
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

Working with Localized Names
-----------------------------

Accessing Localized Names
~~~~~~~~~~~~~~~~~~~~~~~~~

Content items and acts have localized names in different languages:

.. warning::
   Currently localized names are always None, but this example shows how to access them.

.. code-block:: python

   import asyncio
   from valopy import Client, Locals

   async def display_localized_names():
       async with Client(api_key="your-api-key") as client:
           content = await client.get_content(locale=Locals.EN_US)
           
           # Display character with localized names
           for character in content.characters[:3]:
               print(f"\nCharacter: {character.name}")
               if character.localizedNames:
                   print("  Localized names:")
                   # Show a few locales
                   for locale in ['en-US', 'es-ES', 'ja-JP']:
                       if locale in character.localizedNames:
                           print(f"    {locale}: {character.localizedNames[locale]}")

   asyncio.run(display_localized_names())
