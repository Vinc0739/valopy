Best Practices
==============

Follow these best practices when using ValoPy to build robust applications.

General Guidelines
------------------

1. **Always Use Context Managers**
   
   Use ``async with`` for automatic resource cleanup:

   .. code-block:: python

      async with Client(api_key="your-api-key") as client:
          # Client will automatically close when exiting

2. **Handle Errors Gracefully**
   
   Always catch and handle potential exceptions:

   .. code-block:: python

      from valopy.exceptions import ValoPyError
      
      try:
          account = await client.get_account_v1("Name", "TAG")
      except ValoPyError as e:
          print(f"Error: {e}")

3. **Respect Rate Limits**
   
   Implement backoff strategies for rate-limited requests. See :doc:`error_handling` for examples.

4. **Cache Content Data**
   
   Content data changes infrequently. Consider caching it:

   .. code-block:: python

      import asyncio
      from datetime import datetime, timedelta

      class CachedClient:
          def __init__(self, api_key):
              self.client = Client(api_key=api_key)
              self.content_cache = None
              self.cache_time = None
              self.cache_duration = timedelta(hours=1)
          
          async def get_content_cached(self):
              now = datetime.now()
              if (self.content_cache is None or 
                  self.cache_time is None or 
                  now - self.cache_time > self.cache_duration):
                  self.content_cache = await self.client.get_content()
                  self.cache_time = now
              return self.content_cache

5. **Use Type Hints**
   
   ValoPy is fully typed. Leverage this in your code:

   .. code-block:: python

      from valopy import Client
      from valopy.models import AccountV1
      
      async def process_account(account: AccountV1) -> str:
          return f"{account.name}#{account.tag}"

6. **Close Connections Properly**
   
   Always close the client when done (automatic with context manager):

   .. code-block:: python

      client = Client(api_key="your-api-key")
      try:
          # Use client
          pass
      finally:
          await client.close()

Performance Tips
----------------

Concurrent Requests
~~~~~~~~~~~~~~~~~~~

Use ``asyncio.gather`` for concurrent requests:

.. code-block:: python

   async with Client(api_key="your-api-key") as client:
       # Fetch multiple accounts at once
       accounts = await asyncio.gather(
           client.get_account_v1("Player1", "TAG1"),
           client.get_account_v1("Player2", "TAG2"),
           client.get_account_v1("Player3", "TAG3"),
       )

Reuse the Client
~~~~~~~~~~~~~~~~

Create one client instance and reuse it:

.. code-block:: python

   async def main():
       async with Client(api_key="your-api-key") as client:
           # Make multiple requests with the same client
           account1 = await client.get_account_v1("Player1", "TAG1")
           account2 = await client.get_account_v1("Player2", "TAG2")
           content = await client.get_content()

Security Best Practices
-----------------------

Store API Keys Securely
~~~~~~~~~~~~~~~~~~~~~~~~

Never hardcode API keys. Use environment variables:

.. code-block:: python

   import os
   from valopy import Client

   api_key = os.getenv("VALORANT_API_KEY")
   if not api_key:
       raise ValueError("VALORANT_API_KEY environment variable not set")
   
   async with Client(api_key=api_key) as client:
       # Use client

Redact Headers in Logs
~~~~~~~~~~~~~~~~~~~~~~~

The client redacts API keys in debug logs by default:

.. code-block:: python

   # API key is redacted in logs by default
   client = Client(api_key="your-api-key", redact_header=True)
   
   # Only disable if you need to debug authentication issues
   client = Client(api_key="your-api-key", redact_header=False)
