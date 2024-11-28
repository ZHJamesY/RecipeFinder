from flask import Flask
from config import Config
from extensions import db
from controllers.user_controller import user_bp
from controllers.recipe_controller import recipe_bp
from routes.auth_routes import auth_bp
from controllers.index import index
from flask_login import LoginManager
from services.user_service import UserService

user_service = UserService()


# flask app
def create_app():

    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)

    # Register the blueprints
    app.register_blueprint(index)
    app.register_blueprint(recipe_bp, url_prefix='/recipe')
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(auth_bp)

    # Initialize the db object with the app
    db.init_app(app)

    # Create all tables if they don't exist
    with app.app_context():
        # Create the database tables
        db.create_all()

    # Flask-Login setup
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        user = user_service.get_user(user_id)
        return user


    @login_manager.unauthorized_handler
    def unauthorized():
        return "You must be logged in to access this content.", 403

    return app
