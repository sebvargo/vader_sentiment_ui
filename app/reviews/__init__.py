from flask import Blueprint

BP = Blueprint('reviews', import_name=__name__)

from app.reviews import routes