Quick Start
===========

This guide will help you get started with ValoPy quickly.

Installation
------------

.. code-block:: bash

   pip install valopy

Basic Setup
-----------

Initialize the Client
~~~~~~~~~~~~~~~~~~~~~

The simplest way to use ValoPy is with the async context manager:

.. code-block:: python

   import asyncio
   from valopy import Client

   async def main():
       async with Client(api_key="your-api-key-here") as client:
           # Your code here
           pass

   asyncio.run(main())

Manual Connection Management
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you prefer manual control over the connection lifecycle:

.. code-block:: python

   import asyncio
   from valopy import Client

   async def main():
       client = Client(api_key="your-api-key-here")
       try:
           # Your code here
           pass
       finally:
           await client.close()

   asyncio.run(main())

Your First Request
------------------

Fetching Account Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here's a simple example to fetch account information:

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
