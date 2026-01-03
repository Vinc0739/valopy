Examples
========

This page contains simple examples for every implemented endpoint.

Account
-------

Get account information (v2) by name and tag:

.. code-block:: python

   import asyncio
   from valopy import Client

   async def main():
       async with Client(api_key="your-api-key") as client:
           account = await client.get_account_v2(name="PlayerName", tag="TAG")

           print(f"Player: {account.name}#{account.tag}")
           print(f"PUUID: {account.puuid}")
           print(f"Region: {account.region}")
           print(f"Level: {account.account_level}")

   asyncio.run(main())

Content
-------

Get game content like characters, maps, and skins:

.. code-block:: python

   import asyncio
   from valopy import Client, Locale

   async def main():
       async with Client(api_key="your-api-key") as client:
           content = await client.get_content(locale=Locale.EN_US)

           print(f"Version: {content.version}")
           print(f"Characters ({len(content.characters)}):")
           for char in content.characters[:5]:
               print(f"  - {char.name}")

           print(f"Maps ({len(content.maps)}):")
           for map_item in content.maps[:5]:
               print(f"  - {map_item.name}")

   asyncio.run(main())

Version
-------

Get current game version information:

.. code-block:: python

   import asyncio
   from valopy import Client, Region

   async def main():
       async with Client(api_key="your-api-key") as client:
           version = await client.get_version(region=Region.EU)

           print(f"Version: {version.version_for_api}")
           print(f"Branch: {version.branch}")
           print(f"Build: {version.build_ver}")
           print(f"Released: {version.build_date}")

   asyncio.run(main())

Website
-------

Get website news articles:

.. code-block:: python

   import asyncio
   from valopy import Client, CountryCode

   async def main():
       async with Client(api_key="your-api-key") as client:
           articles = await client.get_website(countrycode=CountryCode.EN_US)

           print(f"Latest {min(5, len(articles))} articles:\\n")
           for article in articles[:5]:
               print(f"{article.title}")
               print(f"  {article.category} | {article.date}")
               print(f"  {article.url}\\n")

   asyncio.run(main())

Server Status
-------------

Get current server status:

.. code-block:: python

   import asyncio
   from valopy import Client, Region

   async def main():
       async with Client(api_key="your-api-key") as client:
           status = await client.get_status(region=Region.EU)

           if not status.maintenances and not status.incidents:
               print("All systems operational")
               return

           if status.maintenances:
               print("Maintenances:")
               for m in status.maintenances:
                   if m.titles:
                       print(f"  - {m.titles[0].content}")

           if status.incidents:
               print("\nIncidents:")
               for i in status.incidents:
                   if i.titles:
                       print(f"  - {i.titles[0].content}")

   asyncio.run(main())

Esports Schedule
----------------

Get esports schedule with optional filtering:

.. code-block:: python

   import asyncio
   from valopy import Client, League

   async def main():
       async with Client(api_key="your-api-key") as client:
           # Get esports schedule
           events = await client.get_esports_schedule()

           print(f"Total events: {len(events)}")

           if events:
               event = events[0]
               print(f"Event: {event.league.name}")
               print(f"State: {event.state}")
               print(f"Tournament: {event.tournament.name}")
               if event.match.teams:
                   for team in event.match.teams:
                       print(f"  - {team.name}: {team.game_wins} wins")

           # Filter by league
           vct_events = await client.get_esports_schedule(league=League.VCT_AMERICAS)
           print(f"\nVCT Americas events: {len(vct_events)}")

   asyncio.run(main())


Leaderboard
-----------

Get leaderboard rankings for a region and platform:

.. code-block:: python

   import asyncio
   from valopy import Client, Platform, Region

   async def main():
       async with Client(api_key="your-api-key") as client:
           leaderboard = await client.get_leaderboard(
               region=Region.NA,
               platform=Platform.PC,
               size=10
           )

           print(f"Top {len(leaderboard.players)} Players")
           print(f"Updated: {leaderboard.updated_at}\n")

           for player in leaderboard.players:
               print(f"{player.leaderboard_rank}. {player.name}#{player.tag} - {player.rr} RR ({player.wins} wins)")

           # Show pagination info
           if leaderboard.results:
               print(f"\nTotal players: {leaderboard.results.total}")

   asyncio.run(main())


Queue Status
------------

Get queue status and configurations:

.. code-block:: python

   import asyncio
   from valopy import Client, Region

   async def main():
       async with Client(api_key="your-api-key") as client:
           queues = await client.get_queue_status(region=Region.EU)

           for queue in queues:
               if queue.mode in ["Unrated", "Competitive"]:
                   print(f"\\n{queue.mode}")
                   print(f"  Team Size: {queue.team_size}v{queue.team_size}")
                   print(f"  Party: {queue.party_size.min}-{queue.party_size.max}")
                   print(f"  Required Level: {queue.required_account_level}")

   asyncio.run(main())

Error Handling
--------------

Handle common API errors gracefully:

.. code-block:: python

   import asyncio
   from valopy import (
       Client,
       ValoPyNotFoundError,
       ValoPyPermissionError,
       ValoPyRateLimitError,
       ValoPyRequestError,
   )

   async def main():
       async with Client(api_key="your-api-key") as client:
           try:
               account = await client.get_account_v2_by_puuid(puuid="some-puuid-string")
               print(f"Found: {account.name}#{account.tag}")

           except ValoPyRequestError as e:
               print(f"Request error: {e.message}")

           except ValoPyNotFoundError:
               print("Account not found")

           except ValoPyPermissionError:
               print("Invalid API key")

           except ValoPyRateLimitError as e:
               print(f"Rate limited. Retry after {e.rate_reset}s")

   asyncio.run(main())

Concurrent Requests
-------------------

Fetch multiple accounts concurrently:

.. code-block:: python

   import asyncio
   from valopy import Client

   async def main():
       players = [
           ("Player1", "TAG1"),
           ("Player2", "TAG2"),
           ("Player3", "TAG3"),
       ]

       async with Client(api_key="your-api-key") as client:
           tasks = [client.get_account_v2(name=name, tag=tag) for name, tag in players]
           accounts = await asyncio.gather(*tasks, return_exceptions=True)

           for (name, tag), result in zip(players, accounts):
               if isinstance(result, BaseException):
                   print(f"{name}#{tag}: Error - {result}")
               else:
                   print(f"{name}#{tag}: Level {result.account_level}")

   asyncio.run(main())
