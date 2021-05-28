from flask import render_template
from flask_login import current_user
from utils import social_utils


def render_login(message):
    return render_template("login.html", message=message)


def render_register(message, invalid_password):
    return render_template("register.html", message=message, invalid_password=invalid_password)


def render_home(message):
    posts = social_utils.get_posts()

    user_logged_in = current_user.is_authenticated

    return render_template("index.html", message=message, posts=posts, user_logged_in=user_logged_in)


def render_profile():
    username = current_user.username
    return render_template("profile.html", name=username)


def render_post(message):
    username = current_user.username
    return render_template("post.html", username=username, message=message)
