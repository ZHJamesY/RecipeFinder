from app import create_app
from flask_login import LoginManager
from services.user_service import UserService

user_service = UserService()

# flask app
app = create_app()

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


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="8000")

    # for local testing with https
    # app.run(ssl_context="adhoc", debug=True)
