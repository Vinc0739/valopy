import asyncio

from valopy import Client, ValoPyRateLimitError


async def main():
    async with Client(api_key="your-api-key") as client:
        try:
            # make rapid requests to demonstrate rate limiting
            for i in range(50):
                await client.get_account_v1(name="PlayerName", tag="TAG")
                print(f"Request {i+1}")

        except ValoPyRateLimitError as e:
            # show the rate limit parameters
            print("Rate Limited!")
            print(f"   Limit: {e.rate_limit} requests")
            print(f"   Remaining: {e.rate_remain}")
            print(f"   Reset in: {e.rate_reset} seconds")

            if e.rate_reset:
                # in a real application, you would wait and retry, but for this example, we'll just print a message
                print(f"You need to wait {e.rate_reset} seconds before retrying")


asyncio.run(main())
