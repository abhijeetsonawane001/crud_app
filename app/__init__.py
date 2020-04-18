from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.views.hello import hello

db = SQLAlchemy()


def create_app(config="app.config.ProductionConfig"):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)

    from app.models import User

    app.register_blueprint(hello)
    return app
