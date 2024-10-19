import json
from flask import jsonify

# Specify the path to your JSON file
file_path = './url1data.json'

# Open the JSON file and load its contents
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

recipeInfo = data['results']

for i in range(0, len(recipeInfo)):
    



json_output = json.dumps(recipeInfo, indent=4)  # Use indent for pretty printing
print(json_output)
