from flask import Flask
app = Flask(__name__)


@app.route('/pp')
def hhh():
    return 'Hello, World!'