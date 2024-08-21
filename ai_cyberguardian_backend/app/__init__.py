# app/__init__.py

from flask import Flask
from flask_cors import CORS
from .extensions import db, migrate
from .routes import ai_blueprint
from .config import Config  # Correct import

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Enable CORS for the application
    CORS(app)

    # Initialize database and migration support
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    app.register_blueprint(ai_blueprint)

    return app
