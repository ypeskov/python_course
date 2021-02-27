from gino import Gino

db = Gino()


async def init_db():
    await db.set_bind('postgresql://localhost/homework3', echo=True)

