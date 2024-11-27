from models.user import User
from extensions import db


# Define the service class to handle user-related operations
class UserService:
    # Class methods for querying the database
    def get_user(self, user_id):
        return User.query.filter_by(id=user_id).first()

    def create_user(self, id_, name, email, profile_pic):
        user = User(id=id_, name=name, email=email, profile_pic=profile_pic)
        db.session.add(user)
        db.session.commit()
        print("user committed to database")

    def get_all_recipes_from_user(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        return user.saved_recipes
