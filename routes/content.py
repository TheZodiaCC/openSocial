from flask import Blueprint
import flask_login
from utils import routes_utils

content_ = Blueprint("content", __name__, template_folder='template', static_folder='static')


@content_.route("/")
def home():
    return routes_utils.render_home("")


@content_.route("/profile")
@flask_login.login_required
def profile():
    return routes_utils.render_profile()

