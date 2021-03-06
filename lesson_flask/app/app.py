from flask import Flask, render_template

from views.auth.auth import auth_app

app = Flask(__name__)

app.register_blueprint(auth_app, url_prefix='/auth')


@app.route('/', methods=['GET'], endpoint='home')
def index():
    return render_template('index.html', active_page='home')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
    )
