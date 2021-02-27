import asyncio
from datetime import datetime

from setup import db
from models import User


async def init_db():
    return await db.set_bind('postgresql://localhost/homework3', echo=True)


async def add_users_if_required():
    now = datetime.now()
    user = User(name=f'Yura {now}', username=f'ypeskov-{now}')
    await user.create()


async def main():
    await init_db()
    # await add_users_if_required()

asyncio.run(main())
