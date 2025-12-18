import asyncio

from valopy import Client


async def search_content():
    async with Client(api_key="your-api-key") as client:
        content = await client.get_content()

        # Find a specific character by name
        jett = next((char for char in content.characters if char.name == "Jett"), None)

        if jett:
            print(f"Found: {jett.name}")
            print(f"  ID: {jett.id}")
            print(f"  Asset: {jett.assetName}")

        # Find all active acts
        active_acts = [act for act in content.acts if act.isActive]
        print(f"\nActive Acts: {len(active_acts)}")
        for act in active_acts:
            print(f"  - {act.name}")

        # Get all skins
        print(f"\nTotal Skins: {len(content.skins)}")


asyncio.run(search_content())
