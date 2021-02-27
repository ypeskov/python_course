import asyncio

from setup import db, init_db
from models import User, Post


async def main():
    await init_db()

    res = await Post.delete.gino.status()
    print(res)

    res = await User.delete.gino.status()
    print(res)


if __name__ == '__main__':
    asyncio.run(main())
