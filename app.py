import asyncio
import aiohttp

async def send_request(url, session):
    async with session.post(url) as response:
        return await response.text()

async def main():
    urls = [...]  # List of URLs to send requests to

    async with aiohttp.ClientSession() as session:
        tasks = [send_request(url, session) for url in urls]

        # Gather and execute requests asynchronously
        responses = await asyncio.gather(*tasks)

        # Process responses if needed

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

