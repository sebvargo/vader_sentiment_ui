from flask import render_template, request, jsonify
from app import APP
from app.database import db_session
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

@APP.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@APP.route('/')
def index():
    return render_template('index.html')

@APP.route('/predict', methods = ['POST', 'GET'])
def predict():
    
    if request.method == 'POST':
        
        text     = request.form.get('text')
        analyzer = SentimentIntensityAnalyzer()
        vs       = analyzer.polarity_scores(text)
        
        return jsonify(vs)


    if request.method == 'GET':

        text     = str(request.args['text'])
        analyzer = SentimentIntensityAnalyzer()
        vs       = analyzer.polarity_scores(text)
        
        return jsonify(vs)

