import asyncio

from valopy import Client, Locale


# currently localized names are always None, but this example shows how to access them
async def display_localized_names():
    async with Client(api_key="your-api-key") as client:
        content = await client.get_content(locale=Locale.EN_US)

        # Display character with localized names
        for character in content.characters[:3]:
            print(f"\nCharacter: {character.name}")
            if character.localizedNames:
                print("  Localized names:")
                # Show a few locales
                for locale in ["en-US", "es-ES", "ja-JP"]:
                    if locale in character.localizedNames:
                        print(f"    {locale}: {character.localizedNames[locale]}")


asyncio.run(display_localized_names())
