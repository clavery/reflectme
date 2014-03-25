
from flask_wtf import Form
from wtforms import TextField, TextAreaField
from wtforms.validators import DataRequired, Optional, ValidationError
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound

from .utils import parse_headers
from .models import Path

class PathForm(Form):
    location = TextField('location')
    status = TextField('status', default="200")
    headers = TextAreaField('headers')
    response = TextAreaField('response')

    def validate_headers(form, field):
        if field.data:
            try:
                parse_headers(field.data)
            except:
                raise ValidationError('Headers must be one per-line, with a colon between name and value.')

    def validate_location(form, field):
        if not field.data:
            raise ValidationError('Location is required')

        path = Path.query.filter(Path.location == field.data).first()
        if path:
            raise ValidationError('A Path with that URL already exists')
