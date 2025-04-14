import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'supersecretkey'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///ticketing.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    //UPLOAD_FOLDER = 'app/static/uploads'
    UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'uploads')
    ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'pdf', 'zip'}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB

class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    DEBUG = False
