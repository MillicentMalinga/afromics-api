from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4

# initialise sqlalchemy
db = SQLAlchemy()


# creates unique string for user id
def create_id():
    return uuid4().hex

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(32), primary_key=True, default=create_id)
    email = db.Column(db.String(345), unique=True)
    first_name = db.Column(db.String(256), nullable=False)
    last_name = db.Column(db.String(256), nullable=False)
    bio = db.Column(db.Text, nullable=False)
    occupation = db.Column(db.String(256), nullable=False)
    country = db.Column(db.String(256), nullable=False)
    password = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'bio': self.bio,
            'occupation': self.occupation,
            'country': self.country
        }


    

    