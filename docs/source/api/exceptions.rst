Exceptions
==========

Custom exceptions for error handling.

Exception Hierarchy
-------------------

All Valopy exceptions inherit from the base ``ValoPyError`` class:

.. code-block:: text

   ValoPyError
   └── ValoPyHTTPError
       ├── ValoPyRequestError (400)
       ├── ValoPyPermissionError (401)
       ├── ValoPyNotFoundError (404)
       ├── ValoPyTimeoutError (408)
       ├── ValoPyRateLimitError (429)
       └── ValoPyServerError (5xx)

Base Exceptions
---------------

ValoPyError
~~~~~~~~~~~

.. autoclass:: valopy.exceptions.ValoPyError
   :members:
   :special-members: __init__
   :show-inheritance:

ValoPyHTTPError
~~~~~~~~~~~~~~~

.. autoclass:: valopy.exceptions.ValoPyHTTPError
   :members:
   :special-members: __init__
   :show-inheritance:

HTTP Status Exceptions
----------------------

ValoPyRequestError
~~~~~~~~~~~~~~~~~~

.. autoclass:: valopy.exceptions.ValoPyRequestError
   :members:
   :special-members: __init__
   :show-inheritance:

ValoPyPermissionError
~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: valopy.exceptions.ValoPyPermissionError
   :members:
   :special-members: __init__
   :show-inheritance:

ValoPyNotFoundError
~~~~~~~~~~~~~~~~~~~

.. autoclass:: valopy.exceptions.ValoPyNotFoundError
   :members:
   :special-members: __init__
   :show-inheritance:

ValoPyTimeoutError
~~~~~~~~~~~~~~~~~~

.. autoclass:: valopy.exceptions.ValoPyTimeoutError
   :members:
   :special-members: __init__
   :show-inheritance:

ValoPyRateLimitError
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: valopy.exceptions.ValoPyRateLimitError
   :members:
   :special-members: __init__
   :show-inheritance:

ValoPyServerError
~~~~~~~~~~~~~~~~~

.. autoclass:: valopy.exceptions.ValoPyServerError
   :members:
   :special-members: __init__
   :show-inheritance:

Utility Functions
-----------------

from_client_response_error
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: valopy.exceptions.from_client_response_error
