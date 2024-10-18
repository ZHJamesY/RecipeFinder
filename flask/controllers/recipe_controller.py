from flask import Blueprint, request, jsonify, abort, render_template
import requests
import os

recipe = Blueprint('recipe', __name__)

# allow user find recipe based on their input ingredients
@recipe.route("/find_recipe", methods=['GET'])
def findRecipe():

    # Define the base URL
    url = ' https://api.spoonacular.com/recipes/complexSearch'

    # Define the headers with the x-api-key
    headers = {
        'x-api-key': os.getenv('SPOONACULAR_API')
    }

    # Define the parameters with the ingredients
    params = {
        'includeIngredients': 'chicken',
        'number' : 2,
        'sort' : 'random',
        'type' : 'main course',
        'instructionsRequired' : True,
        'addRecipeInformation' : True,
        'fillIngredients' : False,
    }

    # Make the GET request with the parameters
    response = requests.get(url, params=params, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Print the JSON response if available
        data = response.json()
        return jsonify(data)
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

    return "testing"