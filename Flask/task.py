#!/usr/bin/python3

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

@app.route('/hbnb/c/<text>', strict_slashes=False)
def C(text):
    return f"C {text}"

@app.route('/hbnb/python/<text>', strict_slashes=False)
def Python(text):
    return f"Python {text}"

@app.route('/hbnb/cc/<text>', strict_slashes=False)
def Cc(text='is cool'):
    return f"C {text}"

@app.route('/hbnb/ppython/<text>', strict_slashes=False)
def Ppython(text='is cool'):
    return f"Python {text}"

@app.route('/hbnb/number/<int:n>', strict_slashes=False)
def num(n):
    return f"{n} is a number"


@app.route('/hbnb/number_template/<int:n>', strict_slashes=False)
def num_temp(n=None):
    return render_template('number.html', n=n)

'''
def hello_world():
    return 'Hello World Again'
app.add_url('/', 'hello_world')'''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
