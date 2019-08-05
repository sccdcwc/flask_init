from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    CORS(app, supports_credentials=True)
    db.init_app(app)
    register_blueprint(app)
    return app


def register_blueprint(app_context):
    from app.main import main as main_blueprint
    app_context.register_blueprint(main_blueprint)
