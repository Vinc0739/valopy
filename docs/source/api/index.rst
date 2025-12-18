API Reference
==============

This section provides comprehensive documentation for Valopy's core API, which wraps the `unofficial Valorant API <https://github.com/Henrik-3/unofficial-valorant-api>`_ by `Henrik-3 <https://github.com/Henrik-3>`_.

For information about the underlying API, authentication, and rate limits, see :doc:`../api_backend`.

Library Organization
---------------------

The library is organized into several modules:

**Core Modules:**

* :doc:`client` - Main client interface for interacting with the Valorant API
* :doc:`adapter` - HTTP adapter for making API requests
* :doc:`models` - Data models for API responses
* :doc:`enums` - Enumeration types used throughout the library
* :doc:`exceptions` - Custom exception classes

Module Overview
---------------

Client Module
~~~~~~~~~~~~~

The ``Client`` class is the primary interface for interacting with the Valorant API. It provides async methods for fetching account information, content data, and other resources.

**Key Classes:**

* :py:class:`~valopy.client.Client` - Main client class with context manager support

Adapter Module
~~~~~~~~~~~~~~

The ``adapter`` module handles HTTP requests to the Valorant API. It implements session pooling and connection management.

**Key Features:**

* Session pooling for performance optimization
* Automatic connection lifecycle management
* Lazy logging for efficient operation

Models Module
~~~~~~~~~~~~~

The ``models`` module defines data structures for all API responses. All models use type hints and are fully documented.

**Key Classes:**

* :py:class:`~valopy.models.Result` - Base result wrapper
* :py:class:`~valopy.models.Content` - Content data
* :py:class:`~valopy.models.CardData` - Card information
* :py:class:`~valopy.models.AccountV1` - Account v1 data
* :py:class:`~valopy.models.AccountV2` - Account v2 data

Enums Module
~~~~~~~~~~~~

The ``enums`` module defines enumeration types used throughout the library.

**Key Enums:**

* :py:class:`~valopy.enums.AllowedMethods` - Supported HTTP methods
* :py:class:`~valopy.enums.Locale` - Supported locales/regions

Exceptions Module
~~~~~~~~~~~~~~~~~

The ``exceptions`` module defines custom exception types for error handling.

**Exception Classes:**

* :py:exc:`~valopy.exceptions.ValoPyError` - Base exception
* :py:exc:`~valopy.exceptions.ValoPyHTTPError` - HTTP errors
* And more...

Detailed Documentation
----------------------

.. toctree::
   :maxdepth: 3

   client
   adapter
   models
   enums
   exceptions
