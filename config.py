import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_very_secure_key'  # This is correct, should be set securely
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'license.db')  # Correct for SQLite
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # This is correct
