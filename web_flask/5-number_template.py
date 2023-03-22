#!/usr/bin/python3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def display_hello_hbnb():
    return ("Hello HBNB")

@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    return ("HBNB")

@app.route('/c/<text>', strict_slashes=False)
def dsiplay_text(text):
    return ("C is %s" % text.replace('_' ' '))

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_text_default(text="is cool"):
    return ('Python %s' % text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    return ('%d is a number' % n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def display_html_template(n):
    return (render_template('5-number.html', number=n))


if __name__ == '__main__':
    app.run(host='0.0.0.0', vport=5000, debug=True)
