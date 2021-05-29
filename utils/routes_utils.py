from flask import render_template
from flask_login import current_user
from utils import social_utils


def render_login(error_message):
    return render_template("login.html", error_message=error_message)


def render_register(error_message):
    return render_template("register.html", error_message=error_message)


def render_post_content(post_id, error_message):
    post = social_utils.get_post(post_id)
    username = current_user.username
    comments = list(reversed(post.comments))

    return render_template("post_content.html", post=post, username=username, error_message=error_message, comments=comments)


def render_home(error_message, success_message):
    posts = social_utils.get_posts()

    user_logged_in = current_user.is_authenticated

    if user_logged_in:
        username = current_user.username
    else:
        username = None

    return render_template("index.html", error_message=error_message, posts=posts,
                           user_logged_in=user_logged_in, username=username, success_message=success_message)


def render_profile():
    username = current_user.username
    return render_template("profile.html", username=username)


def render_post(error_message):
    username = current_user.username
    return render_template("post.html", username=username, error_message=error_message)
