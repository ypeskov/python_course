from flask import Blueprint, render_template

from models.database import db
from models.password import Password

pages_app = Blueprint('pages_app', __name__)

url_home = 'home'
url_list_passwords = 'list-passwords'


@pages_app.route('/', methods=['GET'], endpoint=url_home)
def home():
    return render_template('pages/index.html', active_page=url_home)


@pages_app.route('/list-passwords', methods=['GET'], endpoint=url_list_passwords)
def pages():
    passwords = Password.query.all()

    return render_template('pages/list.html', passwords=passwords, active_page=url_list_passwords)
