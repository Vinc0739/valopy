Adapter
=======

The Adapter class handles low-level HTTP communication with the Valorant API.

Adapter Class
-------------

.. autoclass:: valopy.adapter.Adapter
   :members:
   :special-members: __init__, __aenter__, __aexit__
   :member-order: bysource
   :show-inheritance:

Context Manager Usage
---------------------

The Adapter supports async context manager protocol for automatic session cleanup:

.. code-block:: python

   async with Adapter(api_key="your-api-key") as adapter:
       result = await adapter.get("/v1/account/PlayerName/TAG")
       # Adapter will automatically close when exiting the context
