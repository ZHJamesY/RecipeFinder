from app import create_app
# from flask_login import LoginManager
from services.user_service import UserService

user_service = UserService()

# flask app
app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="8000")

    # for local testing with https
    # app.run(ssl_context="adhoc", debug=True)
