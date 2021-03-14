import os
from flask import Flask
from flask_migrate import Migrate

from models.database import db
from views.auth.auth import auth_app
from views.pages.pages import pages_app


app = Flask(__name__)

env = os.environ.get('ENVIRONMENT')
config = 'config.' + env + 'Config'
app.config.from_object(config)

app.secret_key = 'Bubble gum'

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(auth_app, url_prefix='/auth')
app.register_blueprint(pages_app, url_prefix='/')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
    )
