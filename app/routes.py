from flask import render_template
from app import APP
from app.database import db_session

@APP.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@APP.route('/')
def menu():
    return render_template('general/template.html', selection='menu')