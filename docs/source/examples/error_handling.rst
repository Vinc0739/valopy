Error Handling
==============

This guide covers how to handle errors gracefully when using ValoPy.

Basic Error Handling
--------------------

Catching Common Errors
~~~~~~~~~~~~~~~~~~~~~~

Handle common API errors gracefully:

.. code-block:: python

   import asyncio
   from valopy import Client
   from valopy.exceptions import (
       ValoPyNotFoundError,
       ValoPyPermissionError,
       ValoPyRateLimitError,
       ValoPyHTTPError
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
               
           except ValoPyRateLimitError:
               print("Rate limit exceeded. Please try again later.")
               
           except ValoPyHTTPError as e:
               print(f"HTTP Error {e.status_code}: {e.message}")

   asyncio.run(safe_fetch_account())

Advanced Error Handling
-----------------------

Retry Logic with Exponential Backoff
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implement retry logic with exponential backoff for rate-limited requests:

.. code-block:: python

   import asyncio
   from valopy import Client
   from valopy.exceptions import ValoPyRateLimitError, ValoPyHTTPError

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

Exception Hierarchy
-------------------

Understanding ValoPy Exceptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All ValoPy exceptions inherit from ``ValoPyError``:

.. code-block:: text

   ValoPyError
   └── ValoPyHTTPError
       ├── ValoPyRequestError (400)
       ├── ValoPyPermissionError (401)
       ├── ValoPyNotFoundError (404)
       ├── ValoPyTimeoutError (408)
       ├── ValoPyRateLimitError (429)
       └── ValoPyServerError (5xx)

You can catch all HTTP errors with ``ValoPyHTTPError`` or specific ones:

.. code-block:: python

   from valopy.exceptions import ValoPyHTTPError, ValoPyNotFoundError
   try:
       account = await client.get_account_v1("Name", "TAG")
   except ValoPyNotFoundError:
       print("Account doesn't exist")
   except ValoPyHTTPError as e:
       print(f"Other HTTP error: {e.status_code}")
