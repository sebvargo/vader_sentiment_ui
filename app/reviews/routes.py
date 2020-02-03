from flask import render_template, request, jsonify
from app.reviews import BP
from app.database import db_session

@BP.route('/')
def index():
    return render_template('reviews/index.html', selection='reviews')



