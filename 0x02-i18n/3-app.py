#!/usr/bin/env python3
"""
A basic flask app set up.
"""
from flask import Flask, render_template
from flask_babel import Babel, _
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
    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """
    A method to define the index if the application.
    """
    home_title = _('home_title')
    home_header = _('home_header')
    return render_template('3-index.html',
                           home_title=home_title,
                           home_header=home_header)


if __name__ == '__main__':
    app.run()
