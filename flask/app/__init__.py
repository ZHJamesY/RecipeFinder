from flask import Flask
from controllers.index import index

# flask app
def create_app():
    app = Flask(__name__)

    app.register_blueprint(index)


    return app
