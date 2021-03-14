from flask import Blueprint, render_template, request, \
    redirect, url_for, flash

from models.database import db
from models.password import Password

pages_app = Blueprint('pages_app', __name__)

url_home = 'home'
url_list_passwords = 'list-passwords'
url_add_password = 'add-password'
url_create_password = 'create-password'
url_delete_password = 'delete-password'


@pages_app.route('/', methods=['GET'], endpoint=url_home)
def home():
    return render_template('pages/index.html', active_page=url_home)


@pages_app.route('/' + url_list_passwords, methods=['GET'], endpoint=url_list_passwords)
def pages():
    passwords = Password.query.all()

    return render_template('pages/list.html', passwords=passwords, active_page=url_list_passwords)


@pages_app.route('/' + url_add_password, methods=['GET'], endpoint=url_add_password)
def pages():
    passwords = Password.query.all()

    return render_template('pages/add.html', passwords=passwords, active_page=url_add_password)


@pages_app.route('/' + url_create_password, methods=['POST'], endpoint=url_create_password)
def pages():
    form = request.form

    password = Password(resource_name=form['resource_name'],
                        url=form['url'],
                        login=form['login'],
                        password=form['password'],
                        comment=form['comment'])

    try:
        db.session.add(password)
        db.session.commit()
        flash('Your password has been stored')
    except Exception as e:
        flash('Oops, something happened')

    return redirect(url_for('pages_app.' + url_add_password))


@pages_app.route('/'+url_delete_password, methods=['GET'], endpoint=url_delete_password)
def delete_password():
    password_id = request.args.get('id', default=None)

    password = Password.query.filter_by(id=password_id).first_or_404()

    try:
        db.session.delete(password)
        db.session.commit()
        flash('Password was deleted successfully')
    except Exception as e:
        flash('Oops, something happened')

    return redirect(url_for('pages_app.'+url_list_passwords))
