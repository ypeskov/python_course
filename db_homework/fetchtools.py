import asyncio
import json

from loguru import logger
from aiohttp import ClientSession


class DataValueError(Exception):
    pass


async def fetch_data(url: str = None) -> json:
    """
    Fetch data from the URL. The URL must return JSON string
    """
    if url is None:
        raise Exception('url must be a string')

    async with ClientSession() as session:
        response = await session.request(method='GET', url=url)
        if response.status == 200:
            data = await response.text()
            return json.loads(data)
        else:
            raise DataValueError(f'Error getting data. Response code: [{response.status}, {response.reason}]')


async def module_run():
    """
    function to test network connection and fetching of data
    """
    try:
        users = await fetch_data('https://jsonplaceholder.typicode.com/users')
        logger.info(users)
    except DataValueError as e:
        logger.error(e)


if __name__ == '__main__':
    asyncio.run(module_run())
