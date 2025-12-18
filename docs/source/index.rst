Valopy Documentation
====================

Welcome to Valopy's documentation! Valopy is an async API wrapper for the unofficial Valorant API.

.. image:: https://img.shields.io/badge/python-3.14+-blue.svg
   :target: https://www.python.org/downloads/
   :alt: Python Version

Overview
--------

ValoPy provides a simple and intuitive async Python interface to interact with the unofficial Valorant API made by `Henrik-3 <https://github.com/Henrik-3>`_.
It supports fetching account information, content data, and more.

Key Features
~~~~~~~~~~~~

* **Async/Await Support**: Built with asyncio for efficient asynchronous operations
* **Type Hints**: Fully typed for better IDE support and type checking
* **Comprehensive Models**: Well-structured data models for all API responses
* **Error Handling**: Custom exceptions for different error scenarios
* **Performance Optimized**: Session pooling and lazy logging for efficient operations
* **Easy to Use**: Simple and intuitive API design

Quick Start
-----------

Installation
~~~~~~~~~~~~

.. code-block:: bash

   pip install valopy

Basic Usage
~~~~~~~~~~~

.. code-block:: python

   import asyncio
   from valopy import Client

   async def main():
       async with Client(api_key="your-api-key") as client:
           # Get account information (v1)
           account = await client.get_account_v1("PlayerName", "TAG")
           print(f"Account Level: {account.account_level}")
           print(f"Region: {account.region}")

   asyncio.run(main())

Contents
--------

.. toctree::
   :maxdepth: 2
   :caption: API Reference:

   api/index
   api/client
   api/adapter
   api/models
   api/exceptions
   api/enums

.. toctree::
   :maxdepth: 2
   :caption: Examples:

   examples/index

.. toctree::
   :maxdepth: 2
   :caption: Tests:

   tests/index

.. toctree::
   :maxdepth: 2
   :caption: More Information:

   api_backend
   faq
   troubleshooting

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`

