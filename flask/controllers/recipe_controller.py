from flask import Blueprint, request, jsonify
from services.recipe_service import RecipeService

recipe = Blueprint('recipe', __name__)
recipe_manager = RecipeService()


# route return recipe information
@recipe.route("/find_recipe", methods=['GET'])
def findRecipe():

    # Get the ingredients parameter
    ingredients = request.args.get('ingredients')
    if ingredients:
        login = True
        number = 1
        if login:
            number = 4

        return recipe_manager.get_recipe_by_external_api(ingredients, number)

    return jsonify({'error': 'No ingredients provided.'}), 400
