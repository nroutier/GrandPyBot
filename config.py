""" Module that defines the Config class """

import os

class Config(object):
    """ Class that instantiates an object with all needed config files """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-is-secret'
    MAPS_KEY = os.environ.get('MAPS_KEY')
    STATIC_MAPS_KEY = os.environ.get('STATIC_MAPS_KEY')