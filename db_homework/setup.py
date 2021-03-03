from gino import Gino

db = Gino()


async def init_db():
    await db.set_bind('postgresql://postgres:qwerty@localhost/homework3', echo=False)

