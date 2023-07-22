import os
from flask import Flask
from app.routes import bp
from app.models import db

APP: Flask = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(os.getcwd(), 'data.db') 
db.init_app(APP)
with APP.app_context():
    db.create_all()
APP.register_blueprint(bp, url_prefix='/api')

if __name__ == '__main__':
    APP.debug = True
    APP.run()
