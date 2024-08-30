from flask import Flask
from .routes import ai_blueprint, notification_blueprint
from .extensions import db, migrate, socketio
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    socketio.init_app(app)

    app.register_blueprint(ai_blueprint)
    app.register_blueprint(notification_blueprint)

    return app
