from flask import Flask
from controllers.index import index
from controllers.recipe_controller import recipe
from config import Config


# flask app
def create_app():
    app = Flask(__name__)

    # Step 2: Load configuration
    app.config.from_object(Config) # Pass Config class here
    
    app.register_blueprint(index)
    app.register_blueprint(recipe)

    return app
