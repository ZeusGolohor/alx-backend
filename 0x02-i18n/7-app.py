#!/usr/bin/env python3
"""
A basic flask app set up.
"""
from flask import Flask, render_template, g
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
# Fake Database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']
    req_locale = request.accept_languages.best_match(app.config['LANGUAGES'])
    return req_locale if req_locale else app.config['BABEL_DEFAULT_LOCALE']


@babel.timezoneselector
def get_timezone():
    """
    A get_timezone function and use the babel.timezoneselector decorator.
    """
    tz = request.args.get('timezone', '').strip()
    if not tz and g.user:
        tz = g.user['timezone']
    try:
        return pytz.timezone(tz).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


def get_user(user_id):
    """
    Used to get a user from the fake database if it exist.
    """
    return users.get(user_id)


@app.before_request
def before_request():
    """
    A method to run before any request is made.
    """
    user_id = int(request.args.get('login_as'))
    g.user = get_user(user_id) if user_id else None


@app.route('/', strict_slashes=False)
def index():
    """
    A method to define the index if the application.
    A method to determine the welcome message.
    """
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run()
