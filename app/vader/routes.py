from flask import render_template, request, jsonify
from app.vader import BP
from app.database import db_session
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

@BP.route('/')
def index():
    return render_template('vader/index.html', selection='vader')

@BP.route('/predict', methods = ['POST', 'GET'])
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



