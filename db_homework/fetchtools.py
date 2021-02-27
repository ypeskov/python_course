import asyncio
import json

from loguru import logger
from aiohttp import ClientSession


async def fetch_data(url: str = None) -> json:
    if url is None:
        raise Exception('url must be a string')

    async with ClientSession() as session:
        response = await session.request(method='GET', url=url)
        if response.status == 200:
            data = await response.text()
            return json.loads(data)


async def module_run():
    users = await fetch_data('https://jsonplaceholder.typicode.com/users')
    logger.info(users)

if __name__ == '__main__':
    asyncio.run(module_run())
