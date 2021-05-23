from flask import render_template
from flask_login import current_user


def render_login(message):
    return render_template("login.html", message=message)


def render_register(message, invalid_password):
    return render_template("register.html", message=message, invalid_password=invalid_password)


def render_home(message):
    return render_template("index.html", message=message)


def render_profile():
    username = current_user.username
    return render_template("profile.html", name=username)
