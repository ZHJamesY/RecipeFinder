from flask import Blueprint, request, jsonify
from services.user_service import UserService

# Create a Blueprint for the user module
user_bp = Blueprint('user', __name__)

# Initialize the UserService
user_service = UserService()


# Definte the route for getting a user by id
@user_bp.route('/<user_id>', methods=['GET'])
def get_user(user_id):
    # call the get_user method from the user_service
    user = user_service.get_user(user_id)
    print("user id is being called")

    if not user:
        return jsonify({'message': 'User id not found'}), 404

    # Return the user data
    return jsonify({
        'id': user['id'],
        'name': user['name'],
        'email': user['email'],
        'profile_pic': user['profile_pic'],
        # 'saved_recipes': user['saved_recipes']
    })


# Define the route for creating a new user
@user_bp.route('/create', methods=['POST'])
def create_user():
    # Extract the user data from the request
    user_data = request.get_json()
    # Create the user
    user_service.create_user(user_data['id'], user_data['name'],
                             user_data['email'], user_data['profile_pic'])
    # Return a success response
    return jsonify({'message': 'User created successfully'}), 201


# Define the route for getting all recipes from a user
@user_bp.route('/<user_id>/recipes', methods=['GET'])
def get_all_recipes_from_user(user_id):
    # Call the method from the user_service
    recipes = user_service.get_all_recipes_from_user(user_id)
    # Return the list of recipes
    return jsonify([{
        'id': recipe['id'],
        'name': recipe['name'],
        'image_url': recipe['image_url'],
        'ingredients': recipe['ingredients'],
        'instructions': recipe['instructions']
    } for recipe in recipes])


# define the route for adding a recipe to a user
# (no params, using recipe data from request body)
@user_bp.route('/save_recipe', methods=['POST'])
def add_recipe_to_user():
    # extract the recipe data from the request
    recipe_data = request.get_json()

    # extract the email from the recipe data
    email = recipe_data['email']
    # extract the name from the recipe data
    recipe_name = recipe_data['recipe_name']
    # extract the image url from the recipe data
    image_url = recipe_data['image_url']
    # extract the ingredients from the recipe data
    ingredients = recipe_data['ingredients']
    # extract the instructions from the recipe data
    instructions = recipe_data['instructions']

    # check all the elements are present
    if (not email or not recipe_name or not image_url
       or not ingredients or not instructions):
        return jsonify({'error': 'missing recipe data'}), 400

    # try to add the recipe to the user
    try:
        user_service.add_recipe_to_user(
            email,
            recipe_name,
            image_url,
            ingredients,
            instructions
            )
        return jsonify({'message': 'Recipe added to user successfully'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404


# define the route for removing a recipe from a user
# (no params, using recipe name from request body)
@user_bp.route('/remove_recipe', methods=['DELETE'])
def remove_recipe_from_user_with_name():
    recipe_data = request.get_json()
    email = recipe_data['email']
    recipe_name = recipe_data['recipe_name']
    try:
        user_service.remove_recipe_from_user_with_name(email, recipe_name)
        return jsonify(
            {'message': 'Recipe removed from user successfully'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404


# define the route for removing a recipe from a user
# (using recipe id from url params)
# note: this route is not used in our current implementation
@user_bp.route('/<user_id>/remove_recipe', methods=['DELETE'])
def remove_recipe_from_user(user_id, recipe_id):
    try:
        user_service.remove_recipe_from_user(user_id, recipe_id)
        return jsonify(
            {'message': 'Recipe removed from user successfully'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404
