from unittest.mock import patch, MagicMock
from services.recipe_service import RecipeService


# testing for creating a new recipe
@patch.object(RecipeService, "create_recipe")
def test_create_recipe(mock_create_recipe, client):

    new_recipe_data = {
        'name': 'Test Recipe',
        'image_url': 'http://example.com/image.jpg',
        'ingredients': ['ingredient1', 'ingredient2'],
        'instructions': 'Mix ingredients'
    }

    response = client.post(
        '/recipe/create',
        json=new_recipe_data
        )

    # assert status code is 201, json response is correct,
    # and create_recipe was called with the correct arguments
    assert response.status_code == 201
    assert response.json == {'message': 'Recipe created successfully'}
    mock_create_recipe.assert_called_once_with(
        new_recipe_data['name'],
        new_recipe_data['image_url'],
        new_recipe_data['ingredients'],
        new_recipe_data['instructions']
    )


# testing for getting a recipe by id
@patch.object(RecipeService, "get_recipe_by_id")
def test_get_recipe_by_id(mock_get_recipe_by_id, client):
    mock_recipe = {
        'id': 1,
        'name': 'Test Recipe',
        'image_url': 'http://example.com/image.jpg',
        'ingredients': ['ingredient1', 'ingredient2'],
        'instructions': 'Mix ingredients'
    }

    mock_get_recipe_by_id.return_value = mock_recipe

    response = client.get('recipe/1')

    # assert status code is 200, json response is correct,
    # and mock_get_recipe_by_id was called once
    assert response.status_code == 200
    assert response.json == {
        'id': 1,
        'name': 'Test Recipe',
        'image_url': 'http://example.com/image.jpg',
        'ingredients': ['ingredient1', 'ingredient2'],
        'instructions': 'Mix ingredients'
    }
    mock_get_recipe_by_id.assert_called_once()


# testing for getting all recipes
@patch.object(RecipeService, "get_all_recipes")
def test_get_all_recipes(mock_get_all_recipes, client):
    mock_recipe1 = MagicMock(
        id=1,
        name='Test Recipe',
        image_url='http://example.com/image.jpg',
        ingredients=['ingredient1', 'ingredient2'],
        instructions='Mix ingredients'
    )
    mock_recipe1 = {
        'id': 1,
        'name': 'Test Recipe',
        'image_url': 'http://example.com/image.jpg',
        'ingredients': ['ingredient1', 'ingredient2'],
        'instructions': 'Mix ingredients'
    }
    mock_recipe2 = {
        'id': 2,
        'name': 'Test Recipe2',
        'image_url': 'http://example.com/image2.jpg',
        'ingredients': ['ingredient3', 'ingredient4'],
        'instructions': 'Mix ingredients'
    }

    mock_get_all_recipes.return_value = [mock_recipe1, mock_recipe2]

    response = client.get('/recipe/getall')

    # assert status code is 200, json response is correct,
    # and mock_get_all_recipes was called once
    assert response.status_code == 200
    assert response.json == [
        {
            'id': 1,
            'name': 'Test Recipe',
            'image_url': 'http://example.com/image.jpg',
            'ingredients': ['ingredient1', 'ingredient2'],
            'instructions': 'Mix ingredients'
        },
        {
            'id': 2,
            'name': 'Test Recipe2',
            'image_url': 'http://example.com/image2.jpg',
            'ingredients': ['ingredient3', 'ingredient4'],
            'instructions': 'Mix ingredients'
        }
    ]
    mock_get_all_recipes.assert_called_once()
