"""Flask configuration variables."""
from os import path

basedir = path.abspath(path.dirname(__file__))


class Config:
    """Set Flask configuration from .env file."""

    # General Config
    SECRET_KEY = "asdhfjksdahfkjdsahkf"
    FLASK_APP = "kdjfghkjhdsagfjhd"
    FLASK_ENV = "lkjhkjlhkjfdshgk"

    # Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(basedir, 'app.sqlite')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
