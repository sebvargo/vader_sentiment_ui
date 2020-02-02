from flask import Flask
from config import Config
from flask_migrate import Migrate

migrate = Migrate()

def create_app(config_class = Config):
    APP = Flask(__name__)
    APP.config.from_object(config_class)
    
    from app.database import Base
    migrate.init_app(APP, Base)

    from app.general import BP as general_bp
    APP.register_blueprint(general_bp, url_prefix ='/')

    from app.vader import BP as vader_bp
    APP.register_blueprint(vader_bp, url_prefix='/vader')

    return APP

from app.database import models