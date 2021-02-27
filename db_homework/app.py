import asyncio
from datetime import datetime
import json
from asyncpg.exceptions import UniqueViolationError

from setup import db, init_db
from models import User
from fetchtools import fetch_users


async def add_users_if_required():
    now = datetime.now()
    user = User(name=f'Yura {now}', username=f'ypeskov-{now}')
    await user.create()


async def get_users_and_save():
    users = await fetch_users()
    # print(json.dumps(users, indent=4))
    for u in users:
        user = User(name=u['name'], username=u['username'], email=u['email'], phone=u['phone'])
        try:
            await user.create()
        except UniqueViolationError as e:
            print(f'Skipping duplicate: [{user.username}]')


async def main():
    await init_db()
    # await add_users_if_required()
    await asyncio.gather(get_users_and_save())

asyncio.run(main())
