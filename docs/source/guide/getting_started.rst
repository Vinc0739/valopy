Getting Started
===============

This guide will help you get up and running with ValoPy.

Installation
------------

ValoPy requires **Python 3.11+**.

Install from PyPI:

.. code-block:: bash

   pip install valopy

Or with uv:

.. code-block:: bash

   uv add valopy

What is the Unofficial Valorant API?
------------------------------------

ValoPy is a wrapper for the **`Unofficial Valorant API <https://github.com/Henrik-3/unofficial-valorant-api>`_** created by `Henrik-3 <https://github.com/Henrik-3>`_.

The Unofficial Valorant API provides access to Valorant game data that isn't available through official channels. 
It aggregates data from various sources to provide information about:

* **Player accounts** - Names, tags, levels, regions, and player cards
* **Match history** - Detailed match data, scores, and statistics
* **MMR & Ranks** - Competitive rankings and rating history
* **Game content** - Characters (agents), maps, skins, sprays, and more
* **Esports** - Tournament schedules and results
* **Store** - Current store offers and rotations

.. warning::

   This is an **unofficial** API. It is not affiliated with or endorsed by Riot Games.
   Always ensure compliance with the API's usage guidelines.

For more information about the API itself:

* `API Repository <https://github.com/Henrik-3/unofficial-valorant-api>`_
* `API Documentation <https://docs.henrikdev.xyz>`_
* `Discord Server <https://discord.com/invite/X3GaVkX2YN>`_

Getting an API Key
------------------

Before using ValoPy, you need to obtain an API key:

1. Go to the `API Dashboard <https://api.henrikdev.xyz/dashboard>`_
2. Create an account or sign in
3. Generate a new API key
4. Read the **"Before using this API"** section in the API repository

.. tip::

   Keep your API key secure and never commit it to version control.
   Use environment variables or a ``.env`` file to store it.

Quick Start
-----------

Here's a minimal example to fetch account information:

.. code-block:: python

   import asyncio
   from valopy import Client

   async def main():
       async with Client(api_key="your-api-key") as client:
           # Fetch account information
           account = await client.get_account_v1("PlayerName", "TAG")

           print(f"Player: {account.name}#{account.tag}")
           print(f"Level: {account.account_level}")
           print(f"Region: {account.region}")

   asyncio.run(main())