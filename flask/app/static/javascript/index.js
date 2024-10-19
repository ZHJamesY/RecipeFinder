// function fetch data from route /find_recipe when form with id recipeForm is submitted
async function findRecipe() {
    const ingredients = document.getElementById('ingredients').value;
    const resultDiv = document.getElementById('result');
    const images = resultDiv.querySelectorAll('img');


    // get data if input field is not empty
    if (ingredients.trim() != "") {
        const response = await fetch(`/find_recipe?ingredients=${encodeURIComponent(ingredients)}`, {
            method: 'GET',
        });

        // if fetch succssful, display recipe results
        if (response.ok) {
            try {
                const data = await response.json();
                console.log(data.data)
                // display result on webpage
                // document.getElementById('result').innerText = JSON.stringify(data.data[0], null, 2);
                for(let i = 0; i < data.data.length; i++)
                {
                    images[i].src = data.data[i]['image'];
                }

            } catch (error) {
                console.error('Error parsing JSON:', error);
                document.getElementById('result').innerText = 'Error parsing response.';
            }
        } else {
            document.getElementById('result').innerText = 'Error finding recipe.';
        }
    }
}