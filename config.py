import os
import datetime

class DevConfig(object):
    API_BASE_ENDPOINT = "http://localhost:5000/"
    DEBUG = True
    DEVELOPMENT = True
    TESTING = True
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY") 
    DATABASE_DB = os.environ.get("DATABASE_DB")
    DATABASE_HOST = os.environ.get("DATABASE_HOST")
    DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
    DATABASE_USER = os.environ.get("DATABASE_USER")
    DATABASE_PORT = os.environ.get("DATABASE_PORT")
    DATABASE_DIALECT = os.environ.get("DATABASE_DIALECT")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_COMMIT_ON_TREARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATION = True
    # upload file
    IMAGES_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "images")