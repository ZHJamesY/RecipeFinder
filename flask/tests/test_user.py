from unittest.mock import patch, MagicMock
from services.user_service import UserService


# testing for creating a new user
@patch.object(UserService, "create_user")
def test_create_user(mock_create_user, client):
    mock_create_user.return_value = 1

    new_user_data = {
        'id': 1,
        'name': 'Test User',
        'email': 'test@email.com',
        'profile_pic': 'http://example.com/image.jpg'
    }

    response = client.post(
        '/user/create',
        json=new_user_data
        )

    # assert status code is 201, json response is correct,
    # and create_user was called with the correct arguments
    assert response.status_code == 201
    assert response.json == {'message': 'User created successfully'}
    mock_create_user.assert_called_once_with(
        new_user_data['id'],
        new_user_data['name'],
        new_user_data['email'],
        new_user_data['profile_pic']
    )


# testing for getting a user by id
@patch.object(UserService, "get_user")
def test_get_user(mock_get_user, client):
    # mock_user = MagicMock(
    #     id=1,
    #     name='Test User',
    #     email='test@email.com',
    #     profile_pic='http://example.com/image.jpg'
    # )

    mock_user = {
        'id': 1,
        'name': 'Test User',
        'email': 'test@email.com',
        'profile_pic': 'http://example.com/image.jpg'
    }

    mock_get_user.return_value = mock_user

    response = client.get('/user/1')

    # assert status code is 200, json response is correct,
    # and get_user was called once
    assert response.status_code == 200
    assert response.json == {
        'id': 1,
        'name': 'Test User',
        'email': 'test@email.com',
        'profile_pic': 'http://example.com/image.jpg'
    }
    mock_get_user.assert_called_once()


# testing for getting all recipes from a user
@patch.object(UserService, "get_all_recipes_from_user")
def test_get_all_recipes_from_user(mock_get_all_recipes_from_user, client):
    mock_recipe = MagicMock(
        id=1,
        name='Test Recipe1',
        image_url='http://example.com/image.jpg',
        ingredients=['ingredient1', 'ingredient2'],
        instructions='Mix ingredients'
    )

    mock_recipe = {
        'id': 1,
        'name': 'Test Recipe1',
        'image_url': 'http://example.com/image.jpg',
        'ingredients': ['ingredient1', 'ingredient2'],
        'instructions': 'Mix ingredients'
    }

    mock_get_all_recipes_from_user.return_value = [mock_recipe]

    response = client.get('/user/1/recipes')

    # assert status code is 200, json response is correct,
    # and get_all_recipes_from_user was called once
    assert response.status_code == 200
    assert response.json == [{
        'id': 1,
        'name': 'Test Recipe1',
        'image_url': 'http://example.com/image.jpg',
        'ingredients': ['ingredient1', 'ingredient2'],
        'instructions': 'Mix ingredients'
    }]
    mock_get_all_recipes_from_user.assert_called_once()


# testing for adding a recipe to a user
@patch.object(UserService, "add_recipe_to_user")
def test_add_recipe_to_user(mock_add_recipe_to_user, client):
    mock_add_recipe_to_user.return_value = 1

    new_recipe_data = {
        'email': 'test@email.com',
        'recipe_name': 'Test Recipe',
        'image_url': 'http://example.com/image.jpg',
        'ingredients': ['ingredient1', 'ingredient2'],
        'instructions': 'Mix ingredients'
    }

    response = client.post(
        '/user/save_recipe',
        json=new_recipe_data
        )

    # assert status code is 200, json response is correct,
    # and add_recipe_to_user was called once
    assert response.status_code == 200
    assert response.json == {'message': 'Recipe added to user successfully'}
    mock_add_recipe_to_user.assert_called_once_with(
        new_recipe_data['email'],
        new_recipe_data['recipe_name'],
        new_recipe_data['image_url'],
        new_recipe_data['ingredients'],
        new_recipe_data['instructions']
    )


# testing for removing a recipe from a user (using email and name)
@patch.object(UserService, "remove_recipe_from_user_with_name")
def test_remove_recipe_from_user_with_name(
        mock_remove_recipe_from_user_with_name, client):
    mock_remove_recipe_from_user_with_name.return_value = 1

    remove_data = {
        'email': 'test@email.com',
        'recipe_name': 'Test Recipe',
    }

    response = client.delete(
        '/user/remove_recipe',
        json=remove_data
        )

    # assert status code is 200, json response is correct,
    # and remove_recipe_from_user_with_name was called once
    assert response.status_code == 200
    assert response.json == {
        'message': 'Recipe removed from user successfully'}
    mock_remove_recipe_from_user_with_name.assert_called_once_with(
        remove_data['email'],
        remove_data['recipe_name']
    )
