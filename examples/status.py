import asyncio

from valopy import Client, Region


async def get_server_status():
    async with Client(api_key="your-api-key") as client:
        # Fetch server status for Europe region
        status = await client.get_status(region=Region.EU)

        # Check last maintenances
        if not status.maintenances or not status.incidents:
            return

        maintenance = status.maintenances[0]
        print(f"  ID: {maintenance.id}")
        print(f"  Status: {maintenance.maintenance_status}")
        print(f"  Severity: {maintenance.incident_severity}")
        print(f"  Platforms: {', '.join(maintenance.platforms)}")
        print(f"  Created: {maintenance.created_at}")
        if maintenance.titles:
            print(f"  Title: {maintenance.titles[0].content}")
        print()

        # Check last incident
        incident = status.incidents[0]
        print(f"  ID: {incident.id}")
        print(f"  Status: {incident.maintenance_status}")
        print(f"  Severity: {incident.incident_severity}")
        if incident.titles:
            print(f"  Title: {incident.titles[0].content}")
        if incident.updates:
            latest = incident.updates[0]
            if latest.translations:
                print(f"  Message: {latest.translations[0].content}")


asyncio.run(get_server_status())
