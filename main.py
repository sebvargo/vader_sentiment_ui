from app import create_app
from app.database import db_session

APP = create_app()

@APP.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()