import os


class Config:
    CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
    APP_PORT = 8080
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True

    PASSWORD_MIN_LENGTH = 6
    PASSWORD_MAX_LENGTH = 20
    USERNAME_MIN_LENGTH = 3
    USERNAME_MAX_LENGTH = 20
    FORBIDDEN_CHARACTERS = {'~', ':', "'", '+', '[', '\\', '^', '{', '(', '-', '"', '|', ',', '<',
                            '`', '}', '.', '_', '=', ']', '>', ';', ')', '/'}

    POST_TITLE_MIN_LENGTH = 5
    POST_TITLE_MAX_LENGTH = 50
    POST_CONTENT_MIN_LENGTH = 5
    POST_CONTENT_MAX_LENGTH = 250
