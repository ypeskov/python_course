from flask import Blueprint, render_template

auth_app = Blueprint('auth_app', __name__)


@auth_app.route('/login', methods=('GET',), endpoint='login')
def login():
    return render_template('auth/login.html')
