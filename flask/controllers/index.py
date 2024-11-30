from flask import Blueprint, render_template
from flask_login import current_user

index = Blueprint('index', __name__)


@index.route("/")
def home():
    if current_user.is_authenticated:
        return render_template(
            "index.html",
            name=current_user.name,
            email=current_user.email,
            profile_pic=current_user.profile_pic,
        )
    return render_template("index_not_logged_in.html")


@index.route("/saved_recipes_list")
def saved_recipes_list():
    if current_user.is_authenticated:
        return render_template(
            "saved_recipes_list.html",
            email=current_user.email,
            profile_pic=current_user.profile_pic,
            saved_recipes=current_user.saved_recipes,
        )
    return render_template("index_not_logged_in.html")
