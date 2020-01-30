from flask import Flask
from config import Config
from flask_migrate import Migrate

APP = Flask(__name__)
APP.config.from_object(Config)


from app.database import Base
migrate = Migrate(APP, Base)


from app import routes
from app.database import models