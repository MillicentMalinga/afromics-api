from flask import Flask, request, jsonify
from config import ApplicationConfig
from models import db, User
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_object(ApplicationConfig)


db.init_app(app)
bcrypt = Bcrypt(app)

with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register():
    email = request.json['email']
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    bio = request.json['bio']
    password = request.json['password']
    occupation = request.json['occupation']
    country = request.json['country']

    user_found  = User.query.filter_by(email=email).first() is not None

    if user_found:
        return jsonify({
            "error": "User already exists"
        }), 409
    hashed_password = bcrypt.generate_password_hash(password)
    new_user  = User(email=email, first_name=first_name, last_name=last_name, bio=bio, occupation=occupation, country=country, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

    

if __name__ == '__main__':
    app.run(debug=True)