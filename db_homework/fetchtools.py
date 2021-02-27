import asyncio
import loguru
import aiohttp
import json

from aiohttp import ClientSession


async def fetch_users():
    url = 'https://jsonplaceholder.typicode.com/users'

    async with ClientSession() as session:
        response = await session.request(method='GET', url=url)
        if response.status == 200:
            data = await response.text()
            return json.loads(data)


async def module_run():
    users = await fetch_users()
    print(type(users))

if __name__ == '__main__':
    asyncio.run(module_run())
