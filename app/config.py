import os
from secrets import token_hex

BASEDIR_PATH = os.path.dirname(os.path.abspath(__file__))


class BaseConfig:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get(
        "SQLALCHEMY_TRACK_MODIFICATIONS", False
    )
    SQLALCHEMY_ECHO = True
    SECRET_KEY = token_hex(16)

    # Mail Config
    MAIL_SERVER = os.environ.get("MAIL_SERVER", "localhost")
    MAIL_PORT = os.environ.get("MAIL_PORT", "25")
    MAIL_DEFAULT_SENDER = os.environ.get(
        "MAIL_DEFAULT_SENDER", "abhijeet.sonawane001@gmail.com"
    )


class ProductionConfig(BaseConfig):
    pass


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///{}".format(os.path.join(BASEDIR_PATH, "database.db"))
    )


class TestConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///{}".format(os.path.join(BASEDIR_PATH, "database.db"))
    )
