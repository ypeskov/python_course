from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/hello/<name>')
def hello(name):
    return f'Hello, {name}'


if __name__ == '__main__':
    app.run(
        host='localhost',
        port=5000,
        debug=True,
    )
