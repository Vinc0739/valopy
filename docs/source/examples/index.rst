Examples
=========

This section provides practical examples for using Valopy to interact with the `unofficial Valorant API <https://github.com/Henrik-3/unofficial-valorant-api>`_ by `Henrik-3 <https://github.com/Henrik-3>`_. The examples are organized by use case.

Project Examples
----------------

The ValoPy repository includes several complete example scripts in the ``examples/`` directory:

**Available Examples:**

* ``account_v1.py`` - Fetching account information using Account API v1
* ``account_v1_force.py`` - Account API v1 with forced refresh
* ``account_v2.py`` - Fetching account information using Account API v2
* ``advanced_error_handling.py`` - Comprehensive error handling patterns
* ``batch_requests.py`` - Making multiple API requests efficiently
* ``content.py`` - Fetching content data with locale support
* ``content_locale.py`` - Working with locale-specific content
* ``content_localized_names.py`` - Accessing localized content names
* ``content_search.py`` - Searching and filtering content
* ``error_handling.py`` - Basic error handling patterns

Documentation Examples
-----------------------

Quick Start
~~~~~~~~~~~

Get started with ValoPy in minutes:

.. code-block:: python

   import asyncio
   from valopy import Client

   async def main():
       async with Client(api_key="your-api-key") as client:
           account = await client.get_account_v1("PlayerName", "TAG")
           print(f"Account Level: {account.account_level}")

   asyncio.run(main())

Working with Account Data
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 1

   quickstart
   accounts
   content

Error Handling
~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 1

   error_handling
   best_practices

Running Examples
----------------

To run an example from the ``examples/`` directory:

.. code-block:: bash

   # Using Python
   python examples/account_v1.py

   # Using uv (if installed)
   uv run examples/account_v1.py

Make sure you have:

* ValoPy installed (``pip install valopy``)
* A valid Valorant API key set in your environment or passed to the Client
* Python 3.14 or higher

Example Structure
-----------------

Each example file demonstrates a specific use case and includes:

* Clear comments explaining each step
* Proper async/await patterns
* Error handling
* Resource cleanup

This is a great way to learn how to use ValoPy for your specific needs. Start with a simple example and build up to more complex scenarios.
