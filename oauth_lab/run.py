from flask import Flask
from app.routes import bp

APP: Flask = Flask(__name__)
APP.register_blueprint(bp, url_prefix='/api')

if __name__ == '__main__':
    APP.debug = True
    APP.run()
