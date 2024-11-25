from app import create_app

# flask app
app = create_app()

#---------------------------------------------------
#TEMPORARYILY PUTTING ALL LOGIN LOGIC HERE, will put in proper files later

# import os
# import requests
# import json
# from flask import Flask, redirect, request, url_for
# from flask_login import (
#     LoginManager,
#     current_user,
#     login_required,
#     login_user,
#     logout_user,
# )
# from oauthlib.oauth2 import WebApplicationClient

# from models.user import User

# # Google OAuth configuration
# GOOGLE_CLIENT_ID = "42003689246-4t2lkspfbuaf8kccb99srqrlvlpn807u.apps.googleusercontent.com"
# GOOGLE_CLIENT_SECRET = "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"
# GOOGLE_DISCOVERY_URL = (
#     "https://accounts.google.com/.well-known/openid-configuration"
# )

# # Flask app setup
# app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)

# # Flask-Login setup
# login_manager = LoginManager()
# login_manager.init_app(app)

# @login_manager.unauthorized_handler
# def unauthorized():
#     return "You must be logged in to access this content.", 403

# # Flask-Login user loader
# @login_manager.user_loader
# def load_user(user_id):
#     return User.get(user_id)

# # OAuth2 client setup
# client = WebApplicationClient(GOOGLE_CLIENT_ID)

# def get_google_provider_cfg():
#     """Fetch Google provider configuration."""
#     return requests.get(GOOGLE_DISCOVERY_URL).json()

# @app.route("/")
# def index():
#     if current_user.is_authenticated:
#         return (
#             f"<p>Hello, {current_user.name}! You're logged in! Email: {current_user.email}</p>"
#             f"<p>saved recipes: {current_user.saved_recipes}</p>"
#             f"<div><p>Google Profile Picture:</p>"
#             f'<img src="{current_user.profile_pic}" alt="Google profile pic"></img></div>'
#             f'<a class="button" href="/logout">Logout</a>'
#         )
#     else:
#         return '<a class="button" href="/login">Google Login</a>'

# @app.route("/login")
# def login():
#     google_provider_cfg = get_google_provider_cfg()
#     authorization_endpoint = google_provider_cfg["authorization_endpoint"]

#     request_uri = client.prepare_request_uri(
#         authorization_endpoint,
#         redirect_uri=request.base_url + "/callback",
#         scope=["openid", "email", "profile"],
#     )
#     return redirect(request_uri)

# @app.route("/login/callback")
# def callback():
#     code = request.args.get("code")

#     # Fetch token endpoint
#     google_provider_cfg = get_google_provider_cfg()
#     token_endpoint = google_provider_cfg["token_endpoint"]

#     # Exchange authorization code for access token
#     token_url, headers, body = client.prepare_token_request(
#         token_endpoint,
#         authorization_response=request.url,
#         redirect_url=request.base_url,
#         code=code,
#     )
#     token_response = requests.post(
#         token_url,
#         headers=headers,
#         data=body,
#         auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
#     )
#     client.parse_request_body_response(json.dumps(token_response.json()))

#     # Fetch user info endpoint
#     userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
#     uri, headers, body = client.add_token(userinfo_endpoint)
#     userinfo_response = requests.get(uri, headers=headers, data=body)

#     # Ensure email is verified
#     user_data = userinfo_response.json()
#     if user_data.get("email_verified"):
#         unique_id = user_data["sub"]
#         users_email = user_data["email"]
#         picture = user_data["picture"]
#         users_name = user_data["given_name"]
#     else:
#         return "User email not available or not verified by Google.", 400

#     # Retrieve or create user
#     user = User.get(unique_id)
#     if not user:
#         User.create(unique_id, users_name, users_email, picture)

#     # Log in the user
#     user = User.get(unique_id)
#     login_user(user)

#     return redirect(url_for("index"))

# @app.route("/logout")
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for("index"))

# if __name__ == "__main__":
#     app.run(ssl_context="adhoc")

#---------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="8000")
