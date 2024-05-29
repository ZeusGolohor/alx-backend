#!/usr/bin/env python3
"""
A basic flask app set up.
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config():
    """
    A class to configure the application locale.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index():
    """
    A method to define the index if the application.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
