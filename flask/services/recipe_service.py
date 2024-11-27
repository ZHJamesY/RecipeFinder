import os
import requests
from flask import jsonify
from dotenv import load_dotenv
from models.recipe import Recipe
from extensions import db


class RecipeService:
    # method for getting recipe by id
    def get_recipe_by_id(self, recipe_id):
        return Recipe.query.filter_by(id=recipe_id).first()

    #method for getting recipe by html 
    # (might change to name or something)
    def get_recipe_by_html(self, recipe_html):
        return Recipe.query.filter_by(recipe_html=recipe_html).first()

    #method for getting all recipes (that are 
    # currently stored in the database)
    def get_all_recipes(self):
        return Recipe.query.all()
    
    #method for creating a new recipe
    # (to be stored in the db)
    def create_recipe(self, recipe_html):
        recipe = Recipe(recipe_html=recipe_html)
        db.session.add(recipe)
        db.session.commit()
        print("recipe committed to database")

    @staticmethod
    def get_recipe_by_external_api(ingredients, number):
        # Define the base URL
        # url1 finds recipe based on the parameters
        # url2 use recipe id and get recipe ingredients and instructions
        url1 = ' https://api.spoonacular.com/recipes/complexSearch'
        url2 = 'https://api.spoonacular.com/recipes/recipeID/information'

        # load env variables
        load_dotenv()

        # Define the headers with the x-api-key: spoonacular api key
        headers = {
            'x-api-key': os.getenv('SPOONACULAR_API_1')
        }

        # Define the parameters for url1
        params1 = {
            'includeIngredients': ingredients.replace(', ', ','),
            'number': number,
            'sort': 'random',
            # type -> [main course, dessert, side dish,
            # breakfast, appetizer, soup, salad]
            'type': 'main course'
        }

        # Make the GET request to url1, with headers and the parameters
        response1 = requests.get(url1, params=params1, headers=headers)

        finalResponse = []

        if str(response1.status_code).startswith('4'):
            headers['x-api-key'] = os.getenv('SPOONACULAR_API_2')
            response1 = requests.get(url1, params=params1, headers=headers)

        # Check if the request was successful
        if response1.status_code == 200:

            data1 = response1.json()
            recipeInfo = data1['results']

            for r in range(0, len(recipeInfo)):
                finalResponse.append(recipeInfo[r])
                recipeID = str(recipeInfo[r]['id'])
                # makge get request to url2 by extracting recipe id from
                # url1 response and with headers
                response2 = requests.get(url2.replace("recipeID", recipeID), headers=headers)

                if str(response2.status_code).startswith('4'):
                    headers['x-api-key'] = os.getenv('SPOONACULAR_API_2')
                    response2 = requests.get(url2.replace("recipeID", recipeID), headers=headers)

                if response2.status_code == 200:
                    data2 = response2.json()
                    ingredients = data2['extendedIngredients']
                    ingredientsDict = {}

                    for i in range(0, len(ingredients)):
                        ingredientsDict[i] = ingredients[i]['original']

                    finalResponse[r]['preparation'] = ingredientsDict
                    finalResponse[r]['instruction'] = data2['instructions']

                else:
                    # error handling
                    return jsonify({'error': f"Failed to fetch data2. Status code: {response2.status_code}.",
                                    "response": response2.json()}), response2.status_code
            # return final result after cleaning data
            return jsonify({'data': finalResponse})
        else:
            # error handling
            return jsonify({'error': f"Failed to fetch data1. Status code: {response1.status_code}.",
                            "response": response1.json()}), response1.status_code
