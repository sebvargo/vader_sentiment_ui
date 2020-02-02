from flask import Blueprint

BP = Blueprint(
    name        = 'vader', 
    import_name = __name__,
    )

from app.vader import routes

