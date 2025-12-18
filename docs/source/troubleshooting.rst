Troubleshooting Guide
=====================

This guide helps you solve common issues when using ValoPy.

Installation Issues
-------------------

ImportError: No module named 'valopy'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Problem:** You get an error like ``ImportError: No module named 'valopy'`` when trying to import ValoPy.

**Solution:**

1. **Install ValoPy**:

   .. code-block:: bash

      pip install valopy

2. **Check your Python version**:

   .. code-block:: bash

      python --version

   ValoPy requires Python 3.14 or higher.

3. **Verify installation**:

   .. code-block:: bash

      pip list | grep valopy

Connection Issues
-----------------

Connection Timeout
~~~~~~~~~~~~~~~~~~

**Problem:** Your requests to the Valorant API time out after a few seconds.

**Solution:**

1. **Check your internet connection**: Ensure you have a stable internet connection.

2. **Check API status**: The Valorant API might be temporarily unavailable.

3. **Increase timeout** (if ValoPy supports it): Check your ValoPy version for timeout configuration options.

4. **Check firewall/proxy**: Ensure your firewall isn't blocking connections to the API.

401 Unauthorized
~~~~~~~~~~~~~~~~

**Problem:** You get a 401 error when making requests.

**Solution:**

1. **Verify your API key**:

   .. code-block:: python

      from valopy import Client
      
      # Make sure you're passing the correct API key
      async with Client(api_key="your-actual-api-key") as client:
          # ...

2. **Check API key validity**: Your API key might be:
   - Expired or revoked
   - Incorrect or typo'd
   - Invalid format

3. **Regenerate API key**: Try generating a new API key from the API provider.

Rate Limiting
~~~~~~~~~~~~~

**Problem:** You're getting rate limit errors after many requests.

**Solution:**

1. **Add delays between requests**:

   .. code-block:: python

      import asyncio
      from valopy import Client
      
      async def main():
          async with Client(api_key="your-api-key") as client:
              for player in players:
                  account = await client.get_account_v1(player["name"], player["tag"])
                  await asyncio.sleep(1)  # Wait 1 second between requests

2. **Use batch requests efficiently**: Group requests to minimize API calls.

3. **Check rate limits**: The API documentation should specify rate limits.

Async/Await Issues
------------------

TypeError: object NoneType can't be used in 'await' expression
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Problem:** You forget to await an async function.

**Solution:**

Always use ``await`` with async functions:

.. code-block:: python

   import asyncio
   from valopy import Client
   
   async def main():
       async with Client(api_key="your-api-key") as client:
           # ✓ Correct: use await
           account = await client.get_account_v1("Player", "TAG")
           
           # ✗ Wrong: missing await
           # account = client.get_account_v1("Player", "TAG")

RuntimeError: no running event loop
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Problem:** You try to use ValoPy outside an async context.

**Solution:**

Always run async code within an event loop:

.. code-block:: python

   import asyncio
   from valopy import Client
   
   # ✗ Wrong: not in async context
   # account = Client(api_key="...").get_account_v1("Player", "TAG")
   
   # ✓ Correct: use asyncio.run()
   async def main():
       async with Client(api_key="your-api-key") as client:
           account = await client.get_account_v1("Player", "TAG")
           return account
   
   result = asyncio.run(main())

RuntimeError: Cannot use AsyncClient after close()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Problem:** You try to use a closed client.

**Solution:**

Ensure you're using the client within the context manager:

.. code-block:: python

   import asyncio
   from valopy import Client
   
   async def main():
       # ✓ Correct: use async with
       async with Client(api_key="your-api-key") as client:
           account = await client.get_account_v1("Player", "TAG")
   
   # ✗ Wrong: client is closed here
   # account = await client.get_account_v1("Player", "TAG")

Data/Response Issues
--------------------

None values in response
~~~~~~~~~~~~~~~~~~~~~~~

**Problem:** Fields in your response are unexpectedly ``None``.

**Solution:**

1. **Check if field exists**: Some API responses might not include all fields.

2. **Validate response structure**: Print the response to see what you got:

   .. code-block:: python

      import json
      from valopy import Client
      
      async def main():
          async with Client(api_key="your-api-key") as client:
              account = await client.get_account_v1("Player", "TAG")
              print(account)

3. **Use default values**: Handle None gracefully:

   .. code-block:: python

      level = account.account_level or 0
      region = account.region or "Unknown"

KeyError or AttributeError
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Problem:** You get a ``KeyError`` or ``AttributeError`` when accessing fields.

**Solution:**

1. **Check field names**: ValoPy uses snake_case for field names:

   .. code-block:: python

      from valopy import Client
      
      async with Client(api_key="your-api-key") as client:
          account = await client.get_account_v1("Player", "TAG")
          
          # ✓ Correct: snake_case
          level = account.account_level
          
          # ✗ Wrong: camelCase or other format
          # level = account.accountLevel

2. **Check API version**: Different API versions return different fields:

   .. code-block:: python

      # Account v1 has fewer fields than v2
      v1_account = await client.get_account_v1("Player", "TAG")
      v2_account = await client.get_account_v2("Player", "TAG")

3. **Use type hints**: Your IDE can help with autocompletion:

   .. code-block:: python

      from valopy import Client
      from valopy.models import AccountV1
      
      async def main():
          async with Client(api_key="your-api-key") as client:
              account: AccountV1 = await client.get_account_v1("Player", "TAG")
              # Now your IDE knows what fields are available

Testing Issues
--------------

Tests fail with mock fixture errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Problem:** Tests fail with fixture-related errors.

**Solution:**

1. **Ensure conftest.py is present**: Tests require ``tests/unit/conftest.py``

2. **Run tests from repo root**:

   .. code-block:: bash

      cd /path/to/valopy
      pytest tests/unit

3. **Check mock data**: Ensure mock JSON files exist in ``tests/mock/``

Performance Issues
------------------

Requests are slow
~~~~~~~~~~~~~~~~~

**Problem:** Your ValoPy requests are taking longer than expected.

**Solution:**

1. **Check network latency**: Test your connection:

   .. code-block:: bash

      ping api-endpoint.com

2. **Use batch requests**: Make multiple requests concurrently:

   .. code-block:: python

      import asyncio
      from valopy import Client
      
      async def main():
          async with Client(api_key="your-api-key") as client:
              # Make requests concurrently
              tasks = [
                  client.get_account_v1("Player1", "TAG"),
                  client.get_account_v1("Player2", "TAG"),
                  client.get_account_v1("Player3", "TAG"),
              ]
              results = await asyncio.gather(*tasks)

3. **Check for I/O blocking**: Don't use blocking calls in async code:

   .. code-block:: python

      import asyncio
      import time
      from valopy import Client
      
      # ✗ Wrong: blocking call in async code
      async def main():
          async with Client(api_key="your-api-key") as client:
              # time.sleep(1)  # Don't do this!
              
              # ✓ Correct: use async sleep
              await asyncio.sleep(1)

Memory usage is high
~~~~~~~~~~~~~~~~~~~~

**Problem:** Your application uses excessive memory.

**Solution:**

1. **Reuse client connection**: Don't create a new client for each request:

   .. code-block:: python

      import asyncio
      from valopy import Client
      
      async def main():
          # ✓ Correct: reuse client
          async with Client(api_key="your-api-key") as client:
              for player in large_player_list:
                  account = await client.get_account_v1(player["name"], player["tag"])
          
          # ✗ Wrong: creates new client for each request
          # for player in large_player_list:
          #     async with Client(api_key="...") as client:
          #         account = await client.get_account_v1(...)

2. **Process results in batches**: Don't store all results in memory at once.

Still Having Issues?
--------------------

1. **Check the FAQ**: See :doc:`faq` for common questions
2. **Review examples**: Check :doc:`examples/index` for working code
3. **Read API docs**: See :doc:`api/index` for detailed API documentation
4. **Check error details**: Print the full error traceback to understand what went wrong
5. **Search GitHub issues**: Someone else might have experienced the same issue

Getting Help
~~~~~~~~~~~~

If you can't find a solution:

1. Check the repository's issue tracker
2. Review documentation thoroughly
3. Create a minimal reproducible example
4. Report the issue with:
   - Python version
   - ValoPy version
   - Full error traceback
   - Code that reproduces the issue
