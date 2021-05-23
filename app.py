from __init__ import create_app
import os


app = create_app()

APP_PORT = app.config["APP_PORT"]
DEBUG = app.config["DEBUG"]

if __name__ == "__main__":
    app.secret_key = os.urandom(25)
    app.run(debug=DEBUG, host='0.0.0.0', port=APP_PORT, threaded=True)
