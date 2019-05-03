import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-is-secret'
    MAPS_KEY = os.environ.get('MAPS_KEY')