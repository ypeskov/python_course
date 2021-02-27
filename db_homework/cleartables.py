import asyncio

from loguru import logger

from setup import init_db
from models import User, Post


async def clear_tables():
    """
    Clear tables to avoid duplicates
    """
    await init_db()

    logger.info('Cleaning [posts] table')
    res = await Post.delete.gino.status()
    logger.info(res)

    logger.info('Cleaning [users] table')
    res = await User.delete.gino.status()
    logger.info(res)


if __name__ == '__main__':
    asyncio.run(clear_tables())
