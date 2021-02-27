from gino import Gino

from setup import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String, default='')
    username = db.Column(db.String, nullable=False, default='', unique=True)
    email = db.Column(db.String, default='')


if __name__ == '__main__':
    print(db)
