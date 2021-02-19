from flask import Blueprint

# RESTful

bp = Blueprint('auth', __name__, url_prefix='/auth')

from app.blueprints.auth import views, models