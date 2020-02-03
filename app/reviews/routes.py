from flask import render_template, request, jsonify
from app.reviews import BP
from app.database import db_session
import pandas as pd
import os

# get reviews
filepath = os.path.join('app','reviews','data','2000reviews.pk')
assert os.path.isfile(filepath), f"2000 reviews not found in {filepath}"
data = pd.read_pickle(filepath) # columns = ['reviewerID', 'asin', 'reviewerName', 'helpful', 'reviewText', 'overall', 'summary', 'unixReviewTime', 'reviewTime']


@BP.route('/')
def index():
    rnd_sentence = data[['reviewText', 'overall', 'summary']].sample()
    text    = rnd_sentence['reviewText'].values[0]
    rating  = rnd_sentence['overall'].values[0]
    summary = rnd_sentence['summary'].values[0]
    return render_template('reviews/index.html', 
                            selection='reviews', 
                            text = text, 
                            rating = rating, 
                            summary = summary)




