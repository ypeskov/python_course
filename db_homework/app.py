import asyncio
from datetime import datetime
import json
from asyncpg.exceptions import UniqueViolationError
from loguru import logger

from setup import db, init_db
from models import User, Post
from fetchtools import fetch_data
from cleartables import clear_tables


async def add_users_if_required():
    now = datetime.now()
    user = User(name=f'Yura {now}', username=f'ypeskov-{now}')
    await user.create()


async def get_users_and_save():
    logger.info('Starting fetching users')
    users = await fetch_data(url='https://jsonplaceholder.typicode.com/users')
    # print(json.dumps(users, indent=4))
    for u in users:
        user = User(id=u['id'],
                    name=u['name'],
                    username=u['username'],
                    email=u['email'],
                    phone=u['phone'])
        try:
            await user.create()
            logger.info(f'User {user.username} created')
        except UniqueViolationError as e:
            print(f'Skipping duplicate: [{user.username}]')

    logger.info('All users are created')


async def get_posts_and_save():
    logger.info('Starting fetch posts')
    posts = await fetch_data(url='https://jsonplaceholder.typicode.com/posts')
    # print(json.dumps(posts, indent=4))
    for p in posts:
        post = Post(id=p['id'],
                    user_id=p['userId'],
                    title=p['title'],
                    body=p['body'])
        await post.create()
        logger.info(f'Post {post.title} is created')

    logger.info('All posts are created')


async def main():
    await init_db()
    # await add_users_if_required()
    await clear_tables()

    await get_users_and_save()
    await get_posts_and_save()

    await db.pop_bind().close()


asyncio.run(main())
