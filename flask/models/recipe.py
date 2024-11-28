from extensions import db
from models.user_recipe import user_recipe


class Recipe(db.Model):
    __tablename__ = 'recipe'

    # Define table columns
    id = db.Column(db.Integer, primary_key=True)
    # just have one string representing a html line storing
    # all recipe info to keep things simple for now
    recipe_html = db.Column(db.Text, nullable=False)
    users = db.relationship(
        'User',
        secondary=user_recipe,
        back_populates='saved_recipes'
        )

    # should probably use these later
    # title = db.Column(db.String, nullable=False)
    # image = db.Column(db.String, nullable=False)
    # source = db.Column(db.String, nullable=False)
    # url = db.Column(db.String, nullable=False)
    # ingredients = db.Column(db.String, nullable=False)
    # instructions = db.Column(db.String, nullable=False)
