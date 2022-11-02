import os

from flask import Flask

from app.blueprints.index_blueprint import index_blueprint
from app.blueprints.offers_blueprint import offers_blueprint
from app.blueprints.orders_blueprint import orders_blueprint
from app.blueprints.users_blueprint import users_blueprint
from app.config import DevConfig, ProdConfig
from database.create_db import db


def create_app():
    """Создание приложения"""
    app = Flask(__name__)
    app.config.from_object(config_app())
    db.init_app(app)
    app.register_blueprint(index_blueprint)
    app.register_blueprint(users_blueprint)
    app.register_blueprint(orders_blueprint)
    app.register_blueprint(offers_blueprint)
    return app


def config_app():
    """Конфигурирует приложение"""
    if os.getenv('FLASK_DEBUG'):
        return DevConfig
    return ProdConfig
