let recipeInfo;

$(document).ready(function() {

});

function displayRecipeInfo()
{
    document.querySelectorAll('.recipeImage').forEach(image => {
        image.onclick = () => {
            document.querySelector('.recipeInfo').classList.add('scrollable');

            document.querySelector('.popup').style.display = 'flex';
            document.querySelector('.popupImage').src = image.getAttribute('src');

            let index = image.id.split('recipeImage')[1] - 1;
            document.querySelector('#recipeName').innerText = recipeInfo[index]['title'];

            document.querySelector('#instruction').innerText = recipeInfo[index]['instruction'].trimStart().replace(/^(instructions?|Instruction)/i, "").trimStart().replace(/<[^>]*>/g, "");;
            
            let prep = Object.values(recipeInfo[index]['preparation']);
            let prepStr = prep.map(item => `<li>${item}</li>`).join('');

            document.querySelector('#preparation').innerHTML = prepStr;      
        }
    });

    document.querySelector('.popup span').onclick = () => {
        document.querySelector('.popup').style.display = 'none';
    }

}
// function fetch data from route /find_recipe when form with id recipeForm is submitted
async function findRecipe() {
    const fragment = document.createDocumentFragment();
    const imagePromises = []; // Array to hold promises for image loading

    const ingredients = document.getElementById('ingredients').value;
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = `
    <div class="loadingScreen">
        <div class="loader"></div>
    </div>
    <div class="popup">
        <span>&times;</span>
        <div class="recipeContainer">
            <img class="popupImage" src="" alt="Recipe Image">
            <div class="recipeInfo">
                <h1 id="recipeName">Recipe Name</h2>
                <h2>Instructions:</h2>
                <p id="instruction">Recipe Description</p>
                <h2>Preparations:</h2>
                <ul id="preparation">
                </ul>

            </div>
        </div>
    </div>
    `;

    const loader = document.querySelector('.loadingScreen');

    let imagesTagList = [];
    let updateImagesList = [];

    for(let i = 0; i < 4; i++)
    {
        let img = document.createElement('img');
        img.classList.add('recipeImage');
        img.id = 'recipeImage' + (i + 1);
        imagesTagList.push(img);
    }


    // get data if input field is not empty
    if (ingredients.trim() != "") {
        // display loader
        loader.style.display = 'flex';

        const response = await fetch(`/find_recipe?ingredients=${encodeURIComponent(ingredients)}`, {
            method: 'GET',
        });

        // local json file for testing
        // const response = await fetch('http://127.0.0.1:5500/recipefinalreturndata.json');

        // if fetch succssful, display recipe results
        if (response.ok) {
            try {
                const data = await response.json();
                console.log(data.data)
                recipeInfo = data.data; // Store data.data in recipeInfo

                for(let i = 0; i < data.data.length; i++)
                {
                    imagesTagList[i].alt = 'Recipe Image Not Available!';
                    imagesTagList[i].src = data.data[i]['image'];
                    fragment.appendChild(imagesTagList[i]); // Append to fragment instead of directly to resultDiv

                    // Create a promise for each image load
                    imagePromises.push(new Promise((resolve) => {
                        imagesTagList[i].onload = resolve; // Resolve when the image loads
                    }));
                }
                // Wait for all images to load before appending to resultDiv
                Promise.all(imagePromises).then(() => {
                    loader.style.display = 'none';
                    resultDiv.appendChild(fragment);
                    displayRecipeInfo();
                });

            } catch (error) {
                console.log('Error parsing JSON:', error);
                document.getElementById('result').innerText = 'Error parsing response.';
            }
        } else {
            const data = await response.json();
            console.log(data.error)
            document.getElementById('result').innerText = 'Error finding recipe.';
        }
    }
}