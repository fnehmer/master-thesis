from flask import Flask
from flask import Blueprint, request, session, url_for


bp = Blueprint('default', __name__)

@bp.route('/', methods=('GET',))
def portal():
    return "Hello World!"

def create_app(config=None):
    app = Flask(__name__)
    app.register_blueprint(bp, url_prefix='/api')
    return app
