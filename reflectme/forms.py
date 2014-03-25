
from flask_wtf import Form
from wtforms import TextField, TextAreaField
from wtforms.validators import DataRequired

class PathForm(Form):
    location = TextField('location', validators=[DataRequired()])
    status = TextField('status', default="200")
    headers = TextAreaField('headers')
    response = TextAreaField('response')
