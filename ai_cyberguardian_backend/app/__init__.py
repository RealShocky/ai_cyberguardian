from flask import Flask
from .routes import ai_blueprint, notification_blueprint
from .extensions import db, migrate, socketio
from .config import Config
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Load the configuration from Config class
    CORS(app)  # Enable CORS for all routes

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    socketio.init_app(app)

    # Register blueprints
    app.register_blueprint(ai_blueprint)
    app.register_blueprint(notification_blueprint)
    
    return app
