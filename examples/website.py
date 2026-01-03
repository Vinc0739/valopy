import asyncio

from valopy import Client, CountryCode


async def main() -> None:
    async with Client(api_key="your-api-key") as client:
        # Get website content (news articles)
        articles = await client.get_website(countrycode=CountryCode.EN_US)

        print(f"Latest {min(5, len(articles))} articles:\n")
        for article in articles[:5]:
            print(f"{article.title}")
            print(f"  {article.category} | {article.date}")
            print(f"  {article.url}\n")


if __name__ == "__main__":
    asyncio.run(main())
