from flask import Blueprint

BP = Blueprint('general', import_name=__name__)

from app.general import routes