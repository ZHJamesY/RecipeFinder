import os

class Config:
    # Step 1: Set the secret key
    # Set the SECRET_KEY using os.getenv with a default value
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_secret_key') # Add environment variable for SECRET_KEY, with a default value)

    # Step 2: Configure the database URI
    # Set the SQLALCHEMY_DATABASE_URI to use SQLite and define the database name
    SQLALCHEMY_DATABASE_URI = 'sqlite:///recipefinder.db' # Define the database name here'

    # Step 3: Disable SQLAlchemy track modifications
    # Set SQLALCHEMY_TRACK_MODIFICATIONS to False
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Set to False
