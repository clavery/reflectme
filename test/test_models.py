
import json

from . import ReflectMeTest, app

from reflectme.models import Path, Record
from reflectme.database import db

class ModelTests(ReflectMeTest):
    def setUp(self):
        super(ModelTests, self).setUp()

    def tearDown(self):
        super(ModelTests, self).tearDown()

    def test_json_type(self):
        record = Record()

        headers = [('Content-Type', 'application/json'), ('Host', 'www.example.com')]

        record.request_headers = headers

        with app.app_context():
            db.session.add(record)
            db.session.commit()

            rec = record.query.get(record.id)

            assert rec.request_headers[0][0] == 'Content-Type'
            assert rec.request_headers[0][1] == 'application/json'
            assert len(rec.request_headers) == 2
