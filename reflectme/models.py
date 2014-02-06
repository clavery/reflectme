import json

from sqlalchemy.types import TypeDecorator, TEXT

from .database import db


class JSONEncodedDict(TypeDecorator):
    impl = TEXT

    def process_bind_param(self, value, dialect):
        if value is not None:
            value = json.dumps(value)

        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            value = json.loads(value)
        return value


class Path(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(255), index=True)
    content_type = db.Column(db.String(255))
    response = db.Column(db.Text)
    records = db.relationship('Record', backref='path', lazy='joined')


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    path_id = db.Column(db.Integer, db.ForeignKey('path.id'))

    visited = db.Column(db.DateTime)
    request_headers = db.Column(JSONEncodedDict)
    request_body = db.Column(db.Text)
    request_path = db.Column(db.String(255))
    request_method = db.Column(db.String(255))
    request_ip = db.Column(db.String(255))

