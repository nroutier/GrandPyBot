from flask import Flask, current_app
from config import Config
import logging
from logging.handlers import RotatingFileHandler
import os
# from flask_bs4 import Bootstrap
# from flask_fontawesome import FontAwesome

# bootstrap = Bootstrap()
# fontawesome = FontAwesome()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    # bootstrap.init_app(app)
    # fontawesome.init_app(app)

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    if not app.debug and not app.testing:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/grandpybot.log', maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('GrandPYBot startup')

    return app