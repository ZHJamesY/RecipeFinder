from flask import Blueprint, request, jsonify
from services.recipe_service import RecipeService

recipe_bp = Blueprint('recipe', __name__)
recipe_manager = RecipeService()


# Define the route for getting a recipe by id
# note: this route is not used in our current implementation;
#       we only get recipes using the list defined in user model
@recipe_bp.route('/<recipe_id>', methods=['GET'])
def get_recipe_by_id(recipe_id):
    # Call the get_recipe_by_id method from the recipe_service
    recipe = recipe_manager.get_recipe_by_id(recipe_id)

    if not recipe:
        return jsonify({'message': 'Recipe not found'}), 404

    # Return the recipe data
    return jsonify({
        'id': recipe['id'],
        'name': recipe['name'],
        'image_url': recipe['image_url'],
        'ingredients': recipe['ingredients'],
        'instructions': recipe['instructions']
    })


# Define the route for getting a recipe by name
# note: this route is not used in our current implementation
@recipe_bp.route('/<recipe_name>', methods=['GET'])
def get_recipe_by_name(recipe_name):
    # Call the get_recipe_by_name method from the recipe_service
    print(recipe_name)
    recipe = recipe_manager.get_recipe_by_name(recipe_name)

    if not recipe:
        return jsonify({'message': 'Recipe not found'}), 404

    # Return the recipe data
    return jsonify({
        'id': recipe['id'],
        'name': recipe['name'],
        'image_url': recipe['image_url'],
        'ingredients': recipe['ingredients'],
        'instructions': recipe['instructions']
    })


# Define the route for getting all recipes in db
# note: this route is not used in our current implementation
@recipe_bp.route('/getall', methods=['GET'])
def get_all_recipes():
    # Call the get_all_recipes method from the recipe_service
    recipes = recipe_manager.get_all_recipes()

    # Return the list of recipes
    return jsonify([{
        'id': recipe['id'],
        'name': recipe['name'],
        'image_url': recipe['image_url'],
        'ingredients': recipe['ingredients'],
        'instructions': recipe['instructions']
    } for recipe in recipes])


# define the route for creating a new recipe
# (no url params, using recipe data from request body)
@recipe_bp.route('/create', methods=['POST'])
def create_recipe():
    # Extract the recipe data from the request
    recipe_data = request.get_json()
    # Create the recipe
    recipe_manager.create_recipe(
        recipe_data['name'],
        recipe_data['image_url'],
        recipe_data['ingredients'],
        recipe_data['instructions'])

    # Return a success response
    return jsonify({'message': 'Recipe created successfully'}), 201


# route return recipe information
@recipe_bp.route("/find_recipe", methods=['GET'])
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
