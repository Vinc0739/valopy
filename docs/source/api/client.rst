Client
======

The Client class is the main entry point for interacting with the Valorant API.

Client Class
------------

.. autoclass:: valopy.client.Client
   :members:
   :special-members: __init__, __aenter__, __aexit__
   :member-order: bysource
   :show-inheritance:

Context Manager Usage
---------------------

The Client supports async context manager protocol for automatic resource cleanup:

.. code-block:: python

   async with Client(api_key="your-api-key") as client:
       account = await client.get_account_v1("PlayerName", "TAG")
       # Client will automatically close when exiting the context

Manual Usage
------------

If you prefer not to use the context manager, you can manually manage the client lifecycle:

.. code-block:: python

   client = Client(api_key="your-api-key")
   try:
       account = await client.get_account_v1("PlayerName", "TAG")
       print(f"Account Level: {account.account_level}")
   finally:
       await client.close()  # Always close to free resources
