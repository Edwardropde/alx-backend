#!/usr/bin/env python3
"""
Basic Flask app with internationalization support.
"""
from flask_babel import Babel
from flask import Flask, render_template, request


class Config:
    """
    Represents Flask Babel configuration.
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
    determines locale to be used
    """
    locale = request.args.get("locale")
    if locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def hello():
    """renders 0-index.html"""
    return render_template("4-index.html")
