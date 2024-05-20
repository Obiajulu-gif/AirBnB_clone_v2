#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Defines a route for the root URL ("/") of the Flask application. When a GET request is made to this URL, the function `hello_hbnb` is called. This function returns the string "Hello HBNB!".

    Parameters:
        None

    Returns:
        str: The string "Hello HBNB!"

    """
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
