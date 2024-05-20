#!/usr/bin/python3
"""script that starts a Flask web application """

from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """
    Defines a route for the root URL ("/") of the Flask application.
    When a GET request is made to this URL, the function `hello_hbnb`
    is called.
    This function returns the string "Hello HBNB!".

    Parameters:
        None

    Returns:
        str: The string "Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route('/hbnb/')
def hbnb():
    """
    A Flask route decorator that handles requests to the '/hbnb' endpoint.

    Returns:
        str: The string "HBNB".
    """
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """
    A Flask route decorator that handles requests to the
    '/c/<text>' endpoint.

    Args:
        text (str): The text parameter from the URL.

    Returns:
        str: The string "C {text}", where {text} is the input text
        with underscores replaced by spaces.
    """
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """
    A Flask route decorator that handles requests to the
    '/python/<text>' endpoint.

    Args:
        text (str): The text parameter from the URL.

    Returns:
        str: The string "Python {text}", where {text} is
        the input text with underscores replaced by spaces.
    """
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>')
def number_n(n):
    """
    A Flask route decorator that handles requests to
    the '/number/<n>' endpoint .

    Args:
        n (str): The number parameter from the URL.

    Returns:
        str: The string "{n} is a number" if the input
        can be converted to an integer,
        otherwise the string "{n} is not a number".
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_route(n):
    """
    display a HTML page only if n is an integer:
        H1 tag: “Number: n” inside the tag BODY
    Returns:
        html: template displaying the value of n
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """
    A Flask route decorator that handles requests to
    the '/number_odd_or_even/<int:n>' endpoint.

    Args:
        n (int): The number parameter from the URL.

    Returns:
        str: The rendered HTML template '6-number_odd_or_even.html'
        with the value of 'n' passed to it.
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
