from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

# Initialize extensions
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object('config.Config')

    # Initialize extensions
    db.init_app(app)
    Migrate(app, db)
    CORS(app)

    # Register blueprints
    from .routes import ai_blueprint
    app.register_blueprint(ai_blueprint)

    return app
