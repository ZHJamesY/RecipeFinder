from flask import Flask
from controllers.index import index
from controllers.recipe_controller import recipe
from config import Config
from extensions import db
from models.user import User

# flask app
def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config) 
    
    # Register the blueprints
    app.register_blueprint(index)
    app.register_blueprint(recipe)

    # Initialize the database
    # Initialize the db object with the app
    db.init_app(app) 

    # Create all tables if they don't exist
    with app.app_context():
        # Create the database tables
        db.create_all() 

    return app
