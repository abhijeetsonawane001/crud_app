from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()


def create_app(config="app.config.ProductionConfig"):
    app = Flask(__name__)
    app.config.from_object(config)

    # Initialize SQLAlchemy Database
    db.init_app(app)

    # Initialize Migrator
    migrate.init_app(app, db)

    # Initialize Mail
    mail.init_app(app)

    from app.models import User  # noqa 401

    # Import & Register User blueprint
    from app.views.user import user

    app.register_blueprint(user)

    return app
