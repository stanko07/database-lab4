import os
import sys
from flask import Flask
from flasgger import Swagger
from app.config import Config
from app.root import register_routes
from app.database import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Swagger UI
    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": "apispec",
                "route": "/apispec.json",
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/apidocs/"
    }

    swagger_template = {
        "info": {
            "title": "Vacancies Company API",
            "description": "API for managing vacancies, candidates and companies",
            "version": "1.0.0"
        }
    }

    Swagger(app, config=swagger_config, template=swagger_template)

    # SQLAlchemy init
    db.init_app(app)

    # Register routes
    register_routes(app)

    # Detect environment
    is_production = os.environ.get("FLASK_ENV") == "production"

    with app.app_context():
        if not is_production:
            # Only create tables locally!
            print("📌 Local environment detected — running db.create_all()")
            db.create_all()
        else:
            # No table creation in production!
            print("🚀 Production mode — NOT creating tables")

    return app
