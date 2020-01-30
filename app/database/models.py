from sqlalchemy import Column, Integer, String, Unicode, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.database import Base
import datetime


# association_table = Table('association', Base.metadata,
#     Column('review_id', Integer, ForeignKey('reviews.review_id')),
#     Column('votes_id', Integer, ForeignKey('votes.review_id')),
#     Column('predictions_id', Integer, ForeignKey('predictions.review_id')),
#     Column('validated_data_id', Integer, ForeignKey('validated_data.review_id')),
#     Column('votes_id', Integer, ForeignKey('votes.review_id'))
#     )


class Review(Base):
    __tablename__ = 'reviews'
    review_id     = Column(Integer, primary_key = True)
    text          = Column(Unicode(None), unique = True)
    source        = Column(Unicode(50), unique = True)
    
    def __init__(self, text=None, source = 'Online Review'):
        self.text = text
        self.source = source
    
    def __repr__(self):
        return f'<Model:{self.review_id}> \n{self.text}'

class  Vote(Base):
    __tablename__ = 'votes'
    vote_id       = Column(Integer, primary_key = True)
    review_id     = Column(Integer, ForeignKey('reviews.review_id'), nullable=False)
    user_id       = Column(Integer, ForeignKey('users.user_id'), nullable=True)
    tag_id        = Column(Integer, ForeignKey('tags.tag_id'), nullable=True)
    vote          = Column(Unicode(20)) # options = [correct, not sure, incorrect]
    timestamp     = Column(DateTime, index=True, default=datetime.datetime.utcnow)
    



class Prediction(Base):
    __tablename__ = 'predictions'
    prediction_id = Column(Integer, primary_key = True)
    model_id      = Column(Integer, ForeignKey('models.model_id'), nullable=True)
    review_id     = Column(Integer, ForeignKey('reviews.review_id'), nullable=False)
    tag_id        = Column(Integer, ForeignKey('tags.tag_id'), nullable=True)
    timestamp     = Column(DateTime, index=True, default=datetime.datetime.utcnow)

class Tag(Base):
    __tablename__ = 'tags'
    tag_id        = Column(Integer, primary_key = True)
    label         = Column(Unicode(50), unique=True)
    value         = Column(Integer, unique=True)


    def __init__(self, label=None, value = None):
        self.label = label
    
    def __repr__(self):
        return f'<Tag:{self.tag_id}> {self.label}, {self.value}'

class Model(Base):
    __tablename__ = 'models'
    model_id       = Column(Integer, primary_key=True)
    model_name      = Column(Unicode(50), unique=True)
    
    def __init__(self, model_name=None):
        self.model_name = model_name
    
    def __repr__(self):
        return f'<Model:{self.model_id}> {self.model_name}'


class ValidatedData(Base):
    __tablename__= 'validated_data'
    validation_id   = Column(Integer, primary_key = True)
    review_id       = Column(Integer, ForeignKey('reviews.review_id'), nullable=False)
    validated_tags  = Column(Unicode(None), unique=True)
    validation_type = Column(Unicode(50), unique=True)

class User(Base):
    __tablename__ = 'users'
    user_id       = Column(Integer, primary_key=True)
    username      = Column(Unicode(50), unique=True)
    


    def __init__(self, username=None):
        self.username = username

    def __repr__(self):
        return f'<User:{self.user_id}> {self.username}'


