# RecipeFinder  
RecipeFinder Project - OTU  
Access demo at: https://recipefinder-1rqb.onrender.com  
See the related documents/reports in the folder `/documents`

## Project display  
### User not logged in  
https://github.com/user-attachments/assets/75b5a7dc-df2d-4c1a-a36b-6d0c4eb1fe26  

---  

### User logged in  
https://github.com/user-attachments/assets/a1823a81-514a-4925-83a4-074eea18e8cd  

<br/>

# Table of Contents
- [Overview](#overview)  
- [Environment Variables setup](#environment-variables-setup)
- [Deployment](#deployment)  
- [API documentation](#api-documentation)  

<br />

# Overview  
**RecipeFinder** is a web application that allows users to search for recipes based on ingredients they have. The application integrates with the **Spoonacular API** for recipe data and features **Google OAuth** for user authentication. Users can search for recipes, view detailed instructions and ingredients, and save their favorite recipes to their profile.  

---

## Technical Stack  

### Backend:  
- **Flask** web framework for Python  
- **SQLAlchemy** ORM for database management  
- **SQLite** database for data storage  
- **Flask-Login** for user session management  
- **Hypercorn** ASGI server with HTTP1.1 and HTTP/2 support  

### Frontend:  
- **Vanilla JavaScript** for client-side interactions  
- **HTML templates** with Jinja2  
- **CSS** for styling and responsive design  
- **jQuery** for DOM manipulation  

### Authentication & Security:  
- **Google OAuth 2.0** for user authentication  
- **HTTPS** support  
- **Secure session management**  

### DevOps & Deployment:  
- **Docker** containerization  
- **CI/CD pipeline** using GitHub Actions  
- **Automated testing** with pytest, selenium  
- **Code quality checks** with Flake8  
- **Dependabot** for dependency management  

---

## Key Features  

### Recipe Search:  
- Search by ingredients  
- Display multiple recipe results with images  
- Detailed view with instructions and ingredients list  

### User Features:  
- Google account integration  
- Save favorite recipes  
- View saved recipes list  
- Remove saved recipes  

### Responsive Design:  
- Adaptive grid layout for recipe display  
- Mobile-friendly interface  
- Loading animations and interactive elements  

---

## Architecture  
The project follows an **MVC architecture pattern**, with clear separation between models, views, and controllers. The codebase is organized into distinct modules for services, controllers, and routes, making it maintainable and scalable.  

<br />

# Environment Variables setup  

Set up environment variables for spoonacular api key, and Google OAuth 2.0 login features.

**See .env_SAMPLE.txt file for more information.** 

<br />

# Deployment

## Deploy on local machine  

### Run app without docker  
- `pip install -r requirements.txt` to install all required libraries
- Run without hypercorn - Execute the flask/run.py file

- Run with hypercorn - Go to flask directory on terminal, execute command `hypercorn "run:app" -c hypercorn.toml --bind "0.0.0.0:8000"`  

### Run app with Docker    
- Execute the docker_build.bat file or run the commands in the docker_build.bat file to build and run the docker container

    
## Deploy on third-party platform  
- Deploy using Docker, select the Dockerfile file

<br />

# API documentation  

## Interal APIs

### GET - route: '/user/<user_id>'
Used to fetch a user from the database by the ID

### POST - route: '/user/create'
Used to create a new user in the database given the proper JSON body

### GET - route: '/user/<user_id>/recipes'
Used to fetch all of the saved recipes of a user by the ID

### POST - route: '/user/save_recipe'
Used to save a recipe object to the current user given the proper JSON body

### DELETE - route '/user/remove_recipe'
Used to remove a recipe from the current user's saved recipe list given the email and name of the recipe through JSON 

### DELETE - route '/user/<user_id>/remove_recipe'
Used to remove a recipe from a user given the user_id and recipe_id

### GET - route: '/recipe/<recipe_id>'
Used to fetch a recipe from the database by the ID

### GET - route: '/recipe/<recipe_name>'
Used to fetch a recipe from the database by the its name

### GET - route: '/recipe/getall' 
Used to fetch all recipes from the database

### POST - route: '/recipe/create'
Used to create a new recipe in the database

## External APIs - Source: `https://spoonacular.com/food-api`  
 
`GET https://api.spoonacular.com/recipes/complexSearch`  

### Headers  
| Key           | Value                       |
|---------------|-----------------------------|
| `x-api-key` | `YOUR_API_KEY`|  

---

### Query Parameters    

| Parameter          | Type   |  Description                                     |
|--------------------|--------|--------------------------------------------------|
| `includeIngredients` | `string` | Comma-separated list of ingredients to include in the search. Example: `chicken,tomato,garlic` |
| `number`            | `int`    | The number of expected results (between 1 and 100). |
| `sort`              | `string` | Sorting order. Options: `random` (random results) |
| `type`              | `string` | The type of recipe. Example: `main course` See a full list of [Supported Meal Types](https://spoonacular.com/food-api/docs#Meal-Types).|  

--- 
<br/>

`GET https://api.spoonacular.com/recipes/{id}/information`  

### Headers  
| Key           | Value                       |
|---------------|-----------------------------|
| `x-api-key` | `YOUR_API_KEY`|  

---

### Path Parameters  
| Parameter | Type   | Description                               |
|-----------|--------|-------------------------------------------|
| `id`      | `int`  | The unique ID of the recipe. Example: `649495` |  

---  


