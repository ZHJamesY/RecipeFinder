from models.user import User
from extensions import db
from models.recipe import Recipe
from services.recipe_service import RecipeService

recipe_service = RecipeService()


# Define the service class to handle user-related operations
class UserService:
    # Class methods for querying the database
    def get_user(self, user_id):
        return User.query.filter_by(id=user_id).first()

    def get_user_by_email(self, email):
        user = User.query.filter_by(email=email).first()
        if not user:
            print("user not found")
            raise ValueError(f"User with email {email} not found.")
        return user

    def create_user(self, id_, name, email, profile_pic):
        user = User(id=id_, name=name, email=email, profile_pic=profile_pic)
        db.session.add(user)
        db.session.commit()
        print("user committed to database")

    def get_all_recipes_from_user(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        return user.saved_recipes

    def add_recipe_to_user(self, email, recipe_name,
                           image_url, ingredients, instructions):
        user = self.get_user_by_email(email)

        # check if the recipe exists in the database
        recipe = recipe_service.get_recipe_by_name(recipe_name)
        if not recipe:
            # create the recipe if it doesn't exist
            recipe = Recipe(name=recipe_name,
                            image_url=image_url,
                            ingredients=ingredients,
                            instructions=instructions
                            )
            db.session.add(recipe)
            db.session.commit()
            print("recipe committed to database")

        # check if the recipe is already in the user's saved recipes
        if recipe not in user.saved_recipes:
            user.saved_recipes.append(recipe)
            db.session.commit()
            print("recipe added to user")

    def remove_recipe_from_user_with_name(self, email, recipe_name):
        user = self.get_user_by_email(email)

        recipe = recipe_service.get_recipe_by_name(recipe_name)
        if not recipe:
            raise ValueError(f"Recipe with name {recipe_name} not found.")

        if recipe in user.saved_recipes:
            user.saved_recipes.remove(recipe)
            db.session.commit()
            print("recipe removed from user")

    def remove_recipe_from_user(self, user_id, recipe_id):
        user = self.get_user(user_id)
        if not user:
            raise ValueError(f"User with ID {user_id} not found.")

        recipe = Recipe.query.filter_by(id=recipe_id).first()
        if not recipe:
            raise ValueError(f"Recipe with ID {recipe_id} not found.")

        if recipe in user.saved_recipes:
            user.saved_recipes.remove(recipe)
            db.session.commit()
            print("recipe removed from user")
