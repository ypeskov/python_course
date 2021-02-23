from sqlalchemy import (
    Table,
    MetaData,
    create_engine,
    Column,
    Integer,
    String,
    Boolean,
)
from sqlalchemy.orm import mapper

engine = create_engine('sqlite:///example-table.db', echo=True)
metadata = MetaData()

users_table = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String(32), unique=True),
    Column('is_staff', Boolean, nullable=False, default=False, server_default='0') # noqa
)


class User:
    def __init__(self, id: int, username: str, is_staff: bool):
        self.id = id
        self.username = username
        self.is_staff = is_staff


mapper(User, users_table)

if __name__ == '__main__':
    metadata.create_all(engine)
