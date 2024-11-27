from extensions import db

user_recipe = db.Table(
    'user_recipe',
    db.Column('user_id', db.String, db.ForeignKey('user.id'),
              primary_key=True),
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id'),
              primary_key=True)
)
