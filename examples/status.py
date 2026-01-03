import asyncio

from valopy import Client, Region


async def main() -> None:
    async with Client(api_key="your-api-key") as client:
        # Get server status including maintenances and incidents.
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


if __name__ == "__main__":
    asyncio.run(main())
