Supported Endpoints
===================

This page lists all API endpoints that ValoPy currently supports or plans to support.

.. note::

   ✅ = Implemented | ❌ = Not yet implemented

   The wrapper is under active development. More endpoints will be added in future releases.

Account
-------

.. list-table::
   :header-rows: 1
   :widths: 10 50 20 20

   * - Status
     - Endpoint
     - Method
     - Description
   * - ✅
     - ``/v1/account/{name}/{tag}``
     - :meth:`~valopy.client.Client.get_account_v1`
     - Get account by name and tag (V1)
   * - ✅
     - ``/v2/account/{name}/{tag}``
     - :meth:`~valopy.client.Client.get_account_v2`
     - Get account by name and tag (V2)
   * - ❌
     - ``/v1/by-puuid/account/{puuid}``
     - —
     - Get account by PUUID (V1)
   * - ❌
     - ``/v2/by-puuid/account/{puuid}``
     - —
     - Get account by PUUID (V2)

Content
-------

.. list-table::
   :header-rows: 1
   :widths: 10 50 20 20

   * - Status
     - Endpoint
     - Method
     - Description
   * - ✅
     - ``/v1/content``
     - :meth:`~valopy.client.Client.get_content`
     - Get game content (characters, maps, skins, etc.)

Crosshair
---------

.. list-table::
   :header-rows: 1
   :widths: 10 50 20 20

   * - Status
     - Endpoint
     - Method
     - Description
   * - ❌
     - ``/v1/crosshair/generate``
     - —
     - Generate crosshair image

Esports
-------

.. list-table::
   :header-rows: 1
   :widths: 10 50 20 20

   * - Status
     - Endpoint
     - Method
     - Description
   * - ❌
     - ``/v1/esports/schedule``
     - —
     - Get esports schedule

Leaderboard
-----------

.. list-table::
   :header-rows: 1
   :widths: 10 50 20 20

   * - Status
     - Endpoint
     - Method
     - Description
   * - ❌
     - ``/v1/leaderboard/{affinity}``
     - —
     - Get leaderboard (V1)
   * - ❌
     - ``/v2/leaderboard/{affinity}``
     - —
     - Get leaderboard (V2)
   * - ❌
     - ``/v3/leaderboard/{affinity}``
     - —
     - Get leaderboard (V3)

Match
-----

.. list-table::
   :header-rows: 1
   :widths: 10 50 20 20

   * - Status
     - Endpoint
     - Method
     - Description
   * - ❌
     - ``/v2/match/{matchid}``
     - —
     - Get match details (V2)
   * - ❌
     - ``/v4/match/{region}/{matchid}``
     - —
     - Get match details (V4)

Matchlist
---------

.. list-table::
   :header-rows: 1
   :widths: 10 50 20 20

   * - Status
     - Endpoint
     - Method
     - Description
   * - ❌
     - ``/v3/matches/{region}/{name}/{tag}``
     - —
     - Get match history by name (V3)
   * - ❌
     - ``/v4/matches/{region}/{platform}/{name}/{tag}``
     - —
     - Get match history by name (V4)
   * - ❌
     - ``/v3/by-puuid/matches/{region}/{puuid}``
     - —
     - Get match history by PUUID (V3)
   * - ❌
     - ``/v4/by-puuid/matches/{region}/{platform}/{puuid}``
     - —
     - Get match history by PUUID (V4)

MMR
---

.. list-table::
   :header-rows: 1
   :widths: 10 50 20 20

   * - Status
     - Endpoint
     - Method
     - Description
   * - ❌
     - ``/v2/mmr/{region}/{name}/{tag}``
     - —
     - Get MMR by name (V2)
   * - ❌
     - ``/v3/mmr/{region}/{platform}/{name}/{tag}``
     - —
     - Get MMR by name (V3)
   * - ❌
     - ``/v2/by-puuid/mmr/{region}/{puuid}``
     - —
     - Get MMR by PUUID (V2)
   * - ❌
     - ``/v3/by-puuid/mmr/{region}/{platform}/{puuid}``
     - —
     - Get MMR by PUUID (V3)

MMR History
-----------

.. list-table::
   :header-rows: 1
   :widths: 10 50 20 20

   * - Status
     - Endpoint
     - Method
     - Description
   * - ❌
     - ``/v1/mmr-history/{region}/{name}/{tag}``
     - —
     - Get MMR history by name
   * - ❌
     - ``/v1/by-puuid/mmr-history/{region}/{puuid}``
     - —
     - Get MMR history by PUUID (V1)
   * - ❌
     - ``/v2/by-puuid/mmr-history/{region}/{platform}/{puuid}``
     - —
     - Get MMR history by PUUID (V2)

Premier
-------

.. list-table::
   :header-rows: 1
   :widths: 10 50 20 20

   * - Status
     - Endpoint
     - Method
     - Description
   * - ❌
     - ``/v1/premier/{team_id}``
     - —
     - Get premier team info
   * - ❌
     - ``/v1/premier/{team_id}/history``
     - —
     - Get premier team history
   * - ❌
     - ``/v1/premier/conferences/{affinity}/{conference}``
     - —
     - Get conference leaderboard
   * - ❌
     - ``/v1/premier/search``
     - —
     - Search premier teams

Queue Status
------------

.. list-table::
   :header-rows: 1
   :widths: 10 50 20 20

   * - Status
     - Endpoint
     - Method
     - Description
   * - ❌
     - ``/v1/queue-status/{affinity}``
     - —
     - Get queue status

Raw
---

.. list-table::
   :header-rows: 1
   :widths: 10 50 20 20

   * - Status
     - Endpoint
     - Method
     - Description
   * - ❌
     - ``/v1/raw``
     - —
     - Raw match data endpoint

Server Status
-------------

.. list-table::
   :header-rows: 1
   :widths: 10 50 20 20

   * - Status
     - Endpoint
     - Method
     - Description
   * - ❌
     - ``/v1/status/{region}``
     - —
     - Get server status

Store
-----

.. list-table::
   :header-rows: 1
   :widths: 10 50 20 20

   * - Status
     - Endpoint
     - Method
     - Description
   * - ❌
     - ``/v1/store-offers``
     - —
     - Get store offers (V1)
   * - ❌
     - ``/v2/store-offers``
     - —
     - Get store offers (V2)

Stored Data
-----------

.. list-table::
   :header-rows: 1
   :widths: 10 50 20 20

   * - Status
     - Endpoint
     - Method
     - Description
   * - ❌
     - ``/v1/stored-matches/{affinity}``
     - —
     - Get stored matches
   * - ❌
     - ``/v1/stored-mmr-history/{affinity}``
     - —
     - Get stored MMR history

Version
-------

.. list-table::
   :header-rows: 1
   :widths: 10 50 20 20

   * - Status
     - Endpoint
     - Method
     - Description
   * - ❌
     - ``/v1/version/{region}``
     - —
     - Get game version info

Website
-------

.. list-table::
   :header-rows: 1
   :widths: 10 50 20 20

   * - Status
     - Endpoint
     - Method
     - Description
   * - ❌
     - ``/v1/website/{countrycode}``
     - —
     - Get website news
