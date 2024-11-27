from flask import Blueprint, redirect, request, url_for, render_template
from flask_login import login_user, logout_user, login_required

from services.oauth_service import fetch_token, fetch_user_info
from services.user_service import UserService

user_service = UserService()

auth_bp = Blueprint('auth', __name__)


@auth_bp.route("/login")
def login():
    from services.oauth_service import client, get_google_provider_cfg
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)


@auth_bp.route("/login/callback")
def callback():
    code = request.args.get("code")

    # Fetch access token
    token = fetch_token(code, request.url)

    # Fetch user info
    user_data = fetch_user_info(token)

    if not user_data.get("email_verified"):
        return render_template("login_error.html"), 400

    # Retrieve or create user
    unique_id = user_data["sub"]

    # get user from user service
    user = user_service.get_user(unique_id)

    # if user does not exist, create user
    if not user:
        user_service.create_user(
            unique_id, 
            user_data["given_name"], 
            user_data["email"], 
            user_data["picture"])

        # get user again after creating
        user = user_service.get_user(unique_id)
    
    # Log in the user 
    login_user(user)

    return redirect(url_for("index.home"))


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index.home"))
