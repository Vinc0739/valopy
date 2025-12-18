FAQ - Frequently Asked Questions
================================

General Questions
-----------------

What is Valopy?
~~~~~~~~~~~~~~~

Valopy is an async Python wrapper for the `unofficial Valorant API <https://github.com/Henrik-3/unofficial-valorant-api>`_ created by `Henrik-3 <https://github.com/Henrik-3>`_. It provides a type-safe, easy-to-use interface for fetching Valorant player data, content information, and more.

For more information about the underlying API, see :doc:`../api_backend`.

Do I need a Valorant API key?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes, Valopy requires a valid unofficial Valorant API key to make requests. You can obtain an API key from the official Discord server: https://discord.gg/X3GaVkX2YN

For detailed information about authentication and rate limits, see :doc:`../api_backend`.

What Python versions are supported?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ValoPy requires **Python 3.14 or higher**. The library is built with modern Python features including type hints and async/await patterns.

Installation & Setup
--------------------

How do I install Valopy?
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   pip install valopy

Can I use Valopy without asyncio?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Valopy is built on asyncio and designed for async/await usage. If you're not familiar with async Python, consider learning the basics before using Valopy. See the :doc:`examples/index` for async patterns.

How do I set my API key?
~~~~~~~~~~~~~~~~~~~~~~~~

Pass your API key to the ``Client`` constructor:

.. code-block:: python

   from valopy import Client
   
   async with Client(api_key="your-api-key-here") as client:
       # Use client methods here
       pass

Using ValoPy
~~~~~~~~~~~~

What's the difference between AccountV1 and AccountV2?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**AccountV1** provides basic account information, while **AccountV2** includes additional fields and more detailed account data. Most applications should use **AccountV2** for more comprehensive information.

Can I make multiple requests?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes! ValoPy is designed for efficient async operations. You can make multiple concurrent requests:

.. code-block:: python

   import asyncio
   from valopy import Client
   
   async def main():
       async with Client(api_key="your-api-key") as client:
           # Make multiple concurrent requests
           tasks = [
               client.get_account_v1("Player1", "NA1"),
               client.get_account_v1("Player2", "NA1"),
               client.get_account_v1("Player3", "NA1"),
           ]
           results = await asyncio.gather(*tasks)
   
   asyncio.run(main())

How do I fetch content in a specific locale?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pass the locale parameter to content methods:

.. code-block:: python

   from valopy.enums import Locals
   
   async with Client(api_key="your-api-key") as client:
       content = await client.get_content(locale=Locals.EN_US)
       # Content is now in English (US)

Performance & Optimization
--------------------------

Is ValoPy performant?
~~~~~~~~~~~~~~~~~~~~~

Yes. ValoPy includes several performance optimizations:

* **Session pooling** for efficient HTTP connection reuse
* **__slots__** on dataclasses for reduced memory usage
* **Lazy logging** to minimize overhead
* **Async/await** for non-blocking concurrent operations

These optimizations provide **20-40% overall performance improvements** compared to naive implementations.

How many requests can ValoPy handle?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ValoPy can handle thousands of concurrent requests thanks to asyncio. The main limitation is your API rate limits and network bandwidth.

Error Handling
--------------

What exceptions does ValoPy raise?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ValoPy defines several custom exceptions in the :doc:`api/exceptions` module:

* ``ValoPyException`` - Base exception
* ``ClientException`` - Client-level errors
* ``ValidationException`` - Data validation errors
* And more...

See the :doc:`api/exceptions` documentation for the complete list.

How do I handle errors?
~~~~~~~~~~~~~~~~~~~~~~~

Wrap your code in try/except blocks:

.. code-block:: python

   from valopy import Client
   from valopy.exceptions import ValoPyException
   
   async def main():
       try:
           async with Client(api_key="your-api-key") as client:
               account = await client.get_account_v1("Player", "TAG")
       except ValoPyException as e:
           print(f"ValoPy error: {e}")
       except Exception as e:
           print(f"Unexpected error: {e}")

For more examples, see :doc:`examples/error_handling`.

What does a 401 error mean?
~~~~~~~~~~~~~~~~~~~~~~~~~~~

A 401 error typically means your API key is invalid or expired. Check that:

1. Your API key is correct
2. Your API key hasn't expired
3. Your API key has proper permissions

Testing
-------

How do I run tests?
~~~~~~~~~~~~~~~~~~~

Run the test suite with:

.. code-block:: bash

   pytest tests/unit

Or use the convenience script:

.. code-block:: bash

   uv run valopy-test

Can I run a specific test?
~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes, use pytest's file/test selection:

.. code-block:: bash

   # Run a specific test file
   pytest tests/unit/test_account.py
   
   # Run a specific test function
   pytest tests/unit/test_account.py::test_get_account_v1_parsing
   
   # Run tests matching a pattern
   pytest tests/unit -k "account"

Are tests included in the package?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tests are in the repository but not included in the PyPI package. To run tests, clone the repository from GitHub.

Troubleshooting
---------------

I'm getting import errors
~~~~~~~~~~~~~~~~~~~~~~~~~

Make sure ValoPy is installed:

.. code-block:: bash

   pip install valopy

And that you're importing from the correct module:

.. code-block:: python

   from valopy import Client  # ✓ Correct
   from valopy.client import Client  # ✓ Also works
   import valopy  # ✓ Works, but use valopy.Client

My async code is hanging
~~~~~~~~~~~~~~~~~~~~~~~~

Common causes:

1. **Missing await**: Make sure you await async functions
2. **Wrong context manager**: Use ``async with`` not just ``with``
3. **Event loop issues**: Ensure you're running code in an async context

Example:

.. code-block:: python

   import asyncio
   from valopy import Client
   
   async def main():
       async with Client(api_key="your-api-key") as client:
           account = await client.get_account_v1("Player", "TAG")  # ✓ Correct
           # account = client.get_account_v1("Player", "TAG")      # ✗ Wrong
   
   asyncio.run(main())

I need help with a specific error
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Check the :doc:`api/exceptions` documentation to understand what exceptions ValoPy can raise. See the :doc:`examples/error_handling` for error handling patterns.

Contributing
------------

Can I contribute to ValoPy?
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes! Contributions are welcome. Please:

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

More Information
----------------

Where can I find the source code?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ValoPy repository is available on GitHub. Visit the project repository for source code, issues, and discussions.

How do I report bugs?
~~~~~~~~~~~~~~~~~~~~~

Please report bugs on the GitHub issues page. Include:

1. Your Python version
2. Your ValoPy version
3. A minimal reproducible example
4. The full error traceback

Can I use ValoPy in production?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes, ValoPy is suitable for production use. It includes proper error handling, type hints, and comprehensive testing.

However, remember that ValoPy relies on an unofficial Valorant API, so:

* Rate limits may change
* API endpoints may change without notice
* Terms of service should be reviewed before production use
