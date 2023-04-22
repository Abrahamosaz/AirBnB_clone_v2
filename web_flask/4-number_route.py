#!/usr/bin/python3
"""fifth task"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display():
    """display hello HBNB!"""
    return ("hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """display hello HBNB"""
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """display c and text"""
    return ("C %s" % (text.replace('_', ' ')))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """display python and text"""
    return ("Python %s" % (text.replace('_', ' ')))


@app.route('/number/<int:n>', strict_slashes=False)
def print_number(n):
    """print integer value"""
    return ("%d is a number" % (n))


if __name__ == "__main__":
    """the app will not work if imported"""
    app.run(host="0.0.0.0", port=5000)
