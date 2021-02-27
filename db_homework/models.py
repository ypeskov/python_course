from setup import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String, default='')
    username = db.Column(db.String, nullable=False, default='', unique=True)
    email = db.Column(db.String, default='')
    phone = db.Column(db.String(), default='')


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(
        db.ForeignKey('users.id', name='fk_users'),
        nullable=False)
    title = db.Column(db.String(), default='')
    body = db.Column(db.String(), default='')


if __name__ == '__main__':
    print(db)
