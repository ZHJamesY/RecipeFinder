from flask import Blueprint, request, jsonify
from services.recipe_service import RecipeService

recipe_bp = Blueprint('recipe', __name__)
recipe_manager = RecipeService()


# Define the route for getting a recipe by id
@recipe_bp.route('/<recipe_id>', methods=['GET'])
def get_recipe_by_id(recipe_id):
    # Call the get_recipe_by_id method from the recipe_service
    recipe = recipe_manager.get_recipe_by_id(recipe_id)

    if not recipe:
        return jsonify({'message': 'Recipe not found'}), 404

    # Return the recipe data
    return jsonify({
        'id': recipe.id,
        'name': recipe.name,
        'image_url': recipe.image_url,
        'ingredients': recipe.ingredients,
        'instructions': recipe.instructions
    })


# Define the route for getting a recipe by name
@recipe_bp.route('/<recipe_name>', methods=['GET'])
def get_recipe_by_name(recipe_name):
    # Call the get_recipe_by_name method from the recipe_service
    recipe = recipe_manager.get_recipe_by_name(recipe_name)

    if not recipe:
        return jsonify({'message': 'Recipe not found'}), 404

    # Return the recipe data
    return jsonify({
        'id': recipe.id,
        'name': recipe.name,
        'image_url': recipe.image_url,
        'ingredients': recipe.ingredients,
        'instructions': recipe.instructions
    })


# Define the route for getting all recipes
@recipe_bp.route('/getall', methods=['GET'])
def get_all_recipes():
    # Call the get_all_recipes method from the recipe_service
    recipes = recipe_manager.get_all_recipes()

    # Return the list of recipes
    return jsonify([{
        'id': recipe.id,
        'name': recipe.name,
        'image_url': recipe.image_url,
        'ingredients': recipe.ingredients,
        'instructions': recipe.instructions
    } for recipe in recipes])


# define the route for creating a new recipe (default)
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


# Define the route for creating a new recipe (using only html)
@recipe_bp.route('/create', methods=['POST'])
def create_recipe_with_html():
    # Extract the recipe data from the request
    recipe_data = request.get_json()
    # Create the recipe
    recipe_manager.create_recipe_with_html(recipe_data['recipe_html'])
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


# Define the route for getting a recipe by html
# @recipe_bp.route('/html/<recipe_html>', methods=['GET'])
# def get_recipe_by_html(recipe_html):
#     # Call the get_recipe_by_html method from the recipe_service
#     recipe = recipe_manager.get_recipe_by_html(recipe_html)

#     if not recipe:
#         return jsonify({'message': 'Recipe not found'}), 404

#     # Return the recipe data
#     return jsonify({
#         'id': recipe.id,
#         'recipe_html': recipe.recipe_html
#     })

'''
/RECIPEFINDER
    /flask
        /app
            /static
                /css
                    index.css
                /javascript
                    index.js
            /templates
                base.html
                index_not_logged_in.html
                index.html
                login_error.html
            __init__.py
        /controllers
            index.py
            recipe_controller.py
            user_controller.py
        /models
            mode.py
            recipe.py
            user_recipe.py
            user.py
        /routes
            auth_routes.py
        /services
            oauth_service.py
            recipe_service.py
            user_service.py
        /tests
            __init__.py
            conftest.py
            selenium_test.py
        config.py
        extensions.py
        run.py
'''
