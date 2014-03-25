
from flask import Flask

from .database import db
from .models import *
from .views import reflectme

class WSGICopyBody(object):
    def __init__(self, application):
        self.application = application

    def __call__(self, environ, start_response):

        from cStringIO import StringIO
        length = environ.get('CONTENT_LENGTH', '0')
        length = 0 if length == '' else int(length)

        body = environ['wsgi.input'].read(length)
        environ['body_copy'] = body
        environ['wsgi.input'] = StringIO(body)

        # Call the wrapped application
        app_iter = self.application(environ,
                                    self._sr_callback(start_response))

        # Return modified response
        return app_iter

    def _sr_callback(self, start_response):
        def callback(status, headers, exc_info=None):

            # Call upstream start_response
            start_response(status, headers, exc_info)
        return callback

def create_app(database='database.db', testing=False):
    """Application factory"""

    app = Flask(__name__, instance_relative_config=True)
    app.testing = testing

    app.config.from_object('reflectme.settings')
    app.config.from_pyfile('settings.py', silent=True)

    database_uri = 'sqlite:///{0}'.format(database)
    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
    db.init_app(app)

    if not testing:
        with app.app_context():
            db.create_all()

    app.register_blueprint(reflectme)

    app.wsgi_app = WSGICopyBody(app.wsgi_app)
    return app
