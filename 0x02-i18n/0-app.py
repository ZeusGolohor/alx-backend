#!/usr/bin/env python3
"""
A basic flask app set up.
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """
    A method to define the index if the application.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
