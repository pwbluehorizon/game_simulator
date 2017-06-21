from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/game')
def game_view():
    return render_template('game.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
