from flask import render_template, Blueprint, redirect, url_for, request
import flask_login
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from __init__ import db
from utils import routes_utils
from utils import verification_utils

auth_ = Blueprint("auth", __name__, template_folder='template', static_folder='static')


@auth_.route("/register")
def register():
    if flask_login.current_user.is_authenticated:
        return redirect(url_for("content.home"))
    else:
        return render_template("register.html")


@auth_.route("/login")
def login():
    if flask_login.current_user.is_authenticated:
        return redirect(url_for("content.home"))
    else:
        return render_template("login.html")


@auth_.route("/register/process", methods=["POST"])
def register_process():
    if not request.form["name"] or not request.form["password"]:
        return routes_utils.render_register("Passowrd or Username can't be empty", False)
    else:
        name = request.form["name"]
        password = request.form["password"]

        if User.query.filter_by(username=name).first():
            return routes_utils.render_register("Username already taken", False)
        else:
            if verification_utils.check_password(password) and verification_utils.check_username(name):
                new_user = User(username=name, password=generate_password_hash(password, method="sha256"))

                db.session.add(new_user)
                db.session.commit()

                return routes_utils.render_home("Succesfully created an account")
            else:
                message = "Invalid username or password see our guidline about creating accounts"
                return routes_utils.render_register(message, True)


@auth_.route("/login/process", methods=["POST"])
def login_process():
    name = request.form.get("name")
    password = request.form.get("password")

    user = User.query.filter_by(username=name).first()

    if not user or not check_password_hash(user.password, password):
        return routes_utils.render_login("Invalid username or password")

    else:
        flask_login.login_user(user)

        return redirect(url_for("content.profile"))


@auth_.route("/logout", methods=["POST"])
@flask_login.login_required
def logout():
    flask_login.logout_user()

    return redirect(url_for("content.home"))
