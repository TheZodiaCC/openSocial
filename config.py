import os


class Config:
    CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
    APP_PORT = 8080
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True

    PASSWORD_MIN_LENGTH = 6
    PASSWORD_MAX_LENGTH = 20
    USERNAME_MIN_LENGTH = 5
    USERNAME_MAX_LENGTH = 20
    FORBIDDEN_CHARACTERS = {'~', ':', "'", '+', '[', '\\', '^', '{', '(', '-', '"', '|', ',', '<',
                            '`', '}', '.', '_', '=', ']', '>', ';', ')', '/'}
