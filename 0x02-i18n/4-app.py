#!/usr/bin/env python3
"""
A basic flask app set up.
"""
from flask import Flask, render_template
from flask_babel import Babel
from flask import g, request


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


@babel.localeselector
def get_locale():
    """
    A method to determine the best locale for a user using
    the application.
    """
    # To detect if the incoming request contains locale
    # argument and ifs value is a supported locale
    if 'locale' in request.args:
        locale = request.args.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """
    A method to define the index if the application.
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
