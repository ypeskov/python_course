import asyncio
from asyncpg.exceptions import UniqueViolationError
from loguru import logger

from setup import db, init_db
from models import User, Post
from fetchtools import fetch_data
from cleartables import clear_tables


async def create_user(u: User):
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


async def get_users_and_save():
    logger.info('Starting fetching users')
    users = await fetch_data(url='https://jsonplaceholder.typicode.com/users')

    user_lst = []
    for u in users:
        user_lst.append(create_user(u))
    await asyncio.gather(*user_lst)

    logger.info('All users are created')


async def create_post(p):
    post = Post(id=p['id'],
                user_id=p['userId'],
                title=p['title'],
                body=p['body'])
    await post.create()
    logger.info(f'Post {post.title} is created')


async def get_posts_and_save():
    logger.info('Starting fetch posts')
    posts = await fetch_data(url='https://jsonplaceholder.typicode.com/posts')

    posts_lst = []
    for p in posts:
        posts_lst.append(create_post(p))
    await asyncio.gather(*posts_lst)

    logger.info('All posts are created')


async def main():
    await init_db()
    await clear_tables()

    await get_users_and_save()
    await get_posts_and_save()

    await db.pop_bind().close()


asyncio.run(main())
