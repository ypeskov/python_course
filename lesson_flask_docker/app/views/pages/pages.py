from flask import Blueprint, render_template

from models.database import db
from models.password import Password


pages_app = Blueprint('pages_app', __name__)


@pages_app.route('/', methods=['GET'], endpoint='home')
def home():
    return render_template('index.html', active_page='home')


@pages_app.route('/list-passwords', methods=['GET'], endpoint='list-passwords')
def pages():
    passwords = Password.query.all()

    return render_template('pages/list.html', passwords=passwords)
