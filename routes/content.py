from flask import Blueprint, redirect, url_for, request
import flask_login
from utils import routes_utils
from utils import social_utils
from utils import verification_utils
from flask import current_app as app

content_ = Blueprint("content", __name__, template_folder='template', static_folder='static')


@content_.route("/")
def home():
    return routes_utils.render_home(None, None)


@content_.route("/profile")
@flask_login.login_required
def profile():
    return routes_utils.render_profile()


@content_.route("/post")
@flask_login.login_required
def post():
    return routes_utils.render_post(None)


@content_.route("/post_content/<post_id>")
@flask_login.login_required
def post_content(post_id):
    return routes_utils.render_post_content(post_id, None)


@content_.route("/post/commit", methods=["POST"])
@flask_login.login_required
def post_commit():
    if request.form["post-text"] and request.form["post-title"]:
        text = request.form["post-text"]
        title = request.form["post-title"]

        POST_TITLE_MIN_LENGTH = app.config["POST_TITLE_MIN_LENGTH"]
        POST_TITLE_MAX_LENGTH = app.config["POST_TITLE_MAX_LENGTH"]
        POST_CONTENT_MIN_LENGTH = app.config["POST_CONTENT_MIN_LENGTH"]
        POST_CONTENT_MAX_LENGTH = app.config["POST_CONTENT_MAX_LENGTH"]

        if verification_utils.check(text, POST_CONTENT_MAX_LENGTH, POST_CONTENT_MIN_LENGTH, None) and \
                verification_utils.check(title, POST_TITLE_MAX_LENGTH, POST_TITLE_MIN_LENGTH, None):
            username = flask_login.current_user.username

            social_utils.create_post(title, text, username)

            return redirect(url_for("content.home"))
        else:
            return routes_utils.render_post("Invalid title or text")
    else:
        return routes_utils.render_post("Post title and text can't be empty")


@content_.route("/comment/commit/<post_id>", methods=["POST"])
@flask_login.login_required
def comment_commit(post_id):
    if request.form["comment-text"]:
        text = request.form["comment-text"]

        POST_CONTENT_MIN_LENGTH = app.config["POST_CONTENT_MIN_LENGTH"]
        POST_CONTENT_MAX_LENGTH = app.config["POST_CONTENT_MAX_LENGTH"]

        if verification_utils.check(text, POST_CONTENT_MAX_LENGTH, POST_CONTENT_MIN_LENGTH, None):
            username = flask_login.current_user.username

            social_utils.create_comment(text, username, post_id)

            return redirect(url_for("content.post_content", post_id=post_id))
        else:
            return routes_utils.render_post_content(post_id, "Invalid text")
    else:
        return routes_utils.render_post_content(post_id, "Comment text can't be empty")


@content_.errorhandler(401)
def unauthorized(error):
    return redirect(url_for("auth.login"))
