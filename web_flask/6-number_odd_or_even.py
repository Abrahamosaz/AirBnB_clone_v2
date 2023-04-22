#!/usr/bin/python3
"""task six"""
from flask import Flask, render_template
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


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """render template base on the url"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_odd_template(n):
    """render even odd template"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    """the app will not work if imported"""
    app.run(host="0.0.0.0", port=5000)
