from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import app_config




db = SQLAlchemy()  # intialize the SQLAlchemy class


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    from first_flask.user.views import mod
    db.init_app(app)

    # from third_flask.user.views import mod as users_module
    app.register_blueprint(mod)

    return app
