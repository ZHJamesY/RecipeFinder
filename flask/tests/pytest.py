from unittest.mock import patch, MagicMock
from services.recipe_service import RecipeService

from models import Recipe  # Assuming Recipe is imported from models

@patch.object(RecipeService, "create_recipe")
def test_create_recipe():
    # Arrange
    recipe_service = RecipeService()
    name = "Test Recipe"
    image_url = "http://example.com/image.jpg"
    ingredients = ["ingredient1", "ingredient2"]
    instructions = "Mix ingredients"

    # Mock the db session
    with patch('services.recipe_service.db.session') as mock_session:
        # Act
        recipe_service.create_recipe(name, image_url, ingredients, instructions)

        # Assert
        mock_session.add.assert_called_once()
        added_recipe = mock_session.add.call_args[0][0]
        assert added_recipe.name == name
        assert added_recipe.image_url == image_url
        assert added_recipe.ingredients == ingredients
        assert added_recipe.instructions == instructions
        mock_session.commit.assert_called_once()