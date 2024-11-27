from flask import Blueprint, request, jsonify
from services.user_service import UserService

# Create a Blueprint for the user module
user_bp = Blueprint('user', __name__)

#Initialize the UserService
user_service = UserService()

# Definte the route for getting a user
@user_bp.route('/<user_id>', methods=['GET'])
def get_user(user_id):
    #call the get_user method from the user_service
    user = user_service.get_user(user_id)

    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    # Return the user data
    return jsonify({
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'profile_pic': user.profile_pic,
        'saved_recipes': user.saved_recipes
    })

# Define the route for creating a new user
@user_bp.route('/create', methods=['POST'])
def create_user():
    # Extract the user data from the request
    user_data = request.get_json()
    # Create the user
    user_service.create_user(user_data['id'], user_data['name'], user_data['email'], user_data['profile_pic'])
    # Return a success response
    return jsonify({'message': 'User created successfully'}), 201

# Define the route for getting all recipes from a user
@user_bp.route('/<user_id>/recipes', methods=['GET'])
def get_all_recipes_from_user(user_id):
    # Call the method from the user_service
    recipes = user_service.get_all_recipes_from_user(user_id)
    # Return the list of recipes
    return jsonify([{
        'id': recipe.id,
        'recipe_html': recipe.recipe_html
    } for recipe in recipes])