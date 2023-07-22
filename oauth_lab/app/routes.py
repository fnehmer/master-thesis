from flask import Blueprint

bp: Blueprint = Blueprint('default', __name__)

@bp.route('/', methods=(['GET']))
def portal() -> str:
    return "Hello World!"