from flask import Flask
from controllers.index import index
from controllers.recipe_controller import recipe


# flask app
def create_app():
    app = Flask(__name__)

    app.register_blueprint(index)
    app.register_blueprint(recipe)

    return app
