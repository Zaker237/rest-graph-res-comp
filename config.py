import os
import datetime

class Config(object):
    API_BASE_ENDPOINT = "http://localhost:5000/"
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY") 
    DATABASE_DB = os.environ.get("DATABASE_DB")
    DATABASE_HOST = os.environ.get("DATABASE_HOST")
    DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
    DATABASE_USER = os.environ.get("DATABASE_USER")
    DATABASE_PORT = os.environ.get("DATABASE_PORT")
    DATABASE_DIALECT = os.environ.get("DATABASE_DIALECT")
    # upload file
    IMAGES_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "images")