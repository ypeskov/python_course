import os
from flask import Flask

from flask_migrate import Migrate

from models.database import db
from views.auth.auth import auth_app
from views.pages.pages import pages_app

from models.password import Password


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = \
    os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', default=False)

app.secret_key = 'Bubl gum'

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(auth_app, url_prefix='/auth')
app.register_blueprint(pages_app, url_prefix='/')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
    )
