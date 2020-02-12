from flask import render_template, request, jsonify
from app.general import BP
from app.database import db_session
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

@BP.route('/')
def index():
    return render_template('general/template.html', selection='general')




