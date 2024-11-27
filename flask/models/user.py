#represent the user's (account's) info
#since we are only using google oauth
# should store id, name, email, saved recipes, and maybe other user info

from extensions import db
from flask_login import UserMixin
from models.user_recipe import user_recipe

class User(UserMixin, db.Model):
    __tablename__ = 'user'

    # Define table columns
    id = db.Column(db.String, primary_key=True)  # Google user ID
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    profile_pic = db.Column(db.String, nullable=False)
    saved_recipes = db.relationship(
        "Recipe",
        secondary=user_recipe,
        back_populates="users",
    )