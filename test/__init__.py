from unittest import TestCase
import tempfile
import os

from reflectme.app import create_app
from reflectme.database import db

app = create_app(testing=True)

class ReflectMeTest(TestCase):

    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"
        with app.app_context():
            db.create_all()
        self.client = app.test_client()

    def tearDown(self):
        with app.app_context():
            db.drop_all()
