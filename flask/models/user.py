#represent the user's (account's) info
#since we are only using google oauth
# should store id, name, email, saved recipes, and maybe other user info

from extensions import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'user'

    # Define table columns
    id = db.Column(db.String, primary_key=True)  # Google user ID
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    profile_pic = db.Column(db.String, nullable=False)

    # Class methods for querying the database
    @staticmethod
    def get(user_id):
        return User.query.filter_by(id=user_id).first()

    @staticmethod
    def create(id_, name, email, profile_pic):
        user = User(id=id_, name=name, email=email, profile_pic=profile_pic)
        db.session.add(user)
        db.session.commit()
