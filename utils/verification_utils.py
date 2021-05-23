from flask import current_app


def check(value, max_length, min_length, forbidden_chars):
    if len(value) > max_length or len(value) < min_length:
        return False

    for char in value:
        if char in forbidden_chars:
            return False

    return True


def check_password(password):
    max_length = current_app.config["PASSWORD_MAX_LENGTH"]
    min_length = current_app.config["PASSWORD_MIN_LENGTH"]
    forbidden_chars = current_app.config["FORBIDDEN_CHARACTERS"]

    return check(password, max_length, min_length, forbidden_chars)


def check_username(username):
    max_length = current_app.config["USERNAME_MAX_LENGTH"]
    min_length = current_app.config["USERNAME_MIN_LENGTH"]
    forbidden_characters = current_app.config["FORBIDDEN_CHARACTERS"]

    return check(username, max_length, min_length, forbidden_characters)
