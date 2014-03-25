import datetime
import json

from flask import render_template, Blueprint, abort, request, \
        redirect, url_for, render_template
from sqlalchemy.orm.exc import NoResultFound
from pygments import highlight
from pygments.lexers import HttpLexer
from pygments.formatters import HtmlFormatter

from .database import db
from .models import Path, Record
from .forms import PathForm
from .utils import parse_headers

reflectme = Blueprint('reflectme', __name__)

def get_path_instance(location):
    try:
        path = Path.query.filter(Path.location == location).one()
    except NoResultFound:
        abort(404)
    return path

@reflectme.route('/<path:location>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def view_path(location):
    path = get_path_instance(location)

    record = Record()
    record.visited = datetime.datetime.now()
    record.path = path
    record.request_ip = request.remote_addr

    http_request = render_template('http_request.txt', request=request)
    formatted_request = highlight(http_request, HttpLexer(), HtmlFormatter())
    record.request_content = formatted_request

    db.session.add(record)
    db.session.commit()

    headers = parse_headers(path.headers)
    return (path.response, 200, headers)

@reflectme.route('/inspect/<path:location>')
def inspect_path(location):
    path = get_path_instance(location)

    headers = parse_headers(path.headers)
    http_response = render_template('http_response.txt', path=path, headers=headers)
    formatted_response = highlight(http_response, HttpLexer(), HtmlFormatter())

    return render_template('inspect.html', path=path, formatted_response=formatted_response)

@reflectme.route('/', methods=['GET', 'POST'])
def index():
    current_paths = Path.query.all()

    form = PathForm()
    if form.validate_on_submit():
        path = Path()
        form.populate_obj(path)
        db.session.add(path)
        db.session.commit()
        return redirect(url_for('.inspect_path', location=path.location))
    return render_template('index.html', form=form, current_paths=current_paths)

