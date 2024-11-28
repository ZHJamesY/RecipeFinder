from extensions import db
from models.user_recipe import user_recipe
import json


class Recipe(db.Model):
    __tablename__ = 'recipe'

    # Define table columns
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String, nullable=False)
    # source = db.Column(db.String, nullable=False)
    # url = db.Column(db.String, nullable=False)
    ingredients = db.Column(db.String, nullable=False)
    instructions = db.Column(db.String, nullable=False)

    users = db.relationship(
        'User',
        secondary=user_recipe,
        back_populates='saved_recipes'
        )

    def __init__(self, name, image_url, ingredients, instructions):
        self.name = name
        self.image_url = image_url
        self.ingredients = json.dumps(ingredients)  # serialize list to string
        self.instructions = instructions

    @property
    def ingredients_list(self):
        return json.loads(self.ingredients)  # Deserialize JSON string to list

    # just have one string representing a html line storing
    # all recipe info to keep things simple for now
    # recipe_html = db.Column(db.Text, nullable=False)
