import datetime
import json

from flask import render_template, Blueprint, abort, request, \
        redirect, url_for, render_template
from sqlalchemy.orm.exc import NoResultFound

from .database import db
from .models import Path, Record

reflectme = Blueprint('reflectme', __name__)

@reflectme.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'create' in request.args:
            path = Path(location=request.form.get('location'),
                        response=request.form.get('response'),
                        content_type=request.form.get('content_type'))
            db.session.add(path)
            db.session.commit()

            return redirect(url_for('.inspect_path', location=path.location))

def get_path_instance(location):
    try:
        path = Path.query.filter(Path.location == location).one()
    except NoResultFound:
        abort(404)

    return path

@reflectme.route('/<path:location>')
def view_path(location):
    path = get_path_instance(location)

    record = Record()
    record.request_body = request.data
    record.request_headers = request.headers.items()
    record.request_path = request.path
    record.visited = datetime.datetime.now()
    record.path = path
    record.request_method = request.method
    record.request_ip = request.remote_addr

    db.session.add(record)
    db.session.commit()

    return (path.response, 200, {'Content-Type' : path.content_type })

@reflectme.route('/inspect/<path:location>')
def inspect_path(location):
    path = get_path_instance(location)
    return render_template('inspect.html', path=path)

