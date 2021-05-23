from flask import Flask
import flask_login
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    login_manager = flask_login.LoginManager()
    login_manager.init_app(app)

    db.init_app(app)

    from models import User

    @login_manager.user_loader
    def user_loader(user_id):
        return User.query.get(int(user_id))

    with app.app_context():
        db.create_all()

        from routes import content, auth

        app.register_blueprint(content.content_)
        app.register_blueprint(auth.auth_)

        return app
