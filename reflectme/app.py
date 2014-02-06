
from flask import Flask

from .database import db
from .models import *
from .views import reflectme

def create_app(testing=False):
    """Application factory"""

    app = Flask(__name__, instance_relative_config=True)
    app.testing = testing

    app.config.from_object('reflectme.settings')
    app.config.from_pyfile('settings.py', silent=True)

    db.init_app(app)

    if not testing:
        with app.app_context():
            db.create_all()

    app.register_blueprint(reflectme)

    return app
