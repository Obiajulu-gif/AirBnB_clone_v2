#!/usr/bin/python3
"""script that starts a Flask web application """

from flask import Flask
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
