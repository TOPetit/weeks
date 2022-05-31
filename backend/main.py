from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import re
import uuid
from werkzeug.security import generate_password_hash, check_password_hash

regex_mail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

app = Flask(__name__)

app.config["SECRET_KEY"] = 'secret'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

db = SQLAlchemy(app)

class User(db.Model):
    email = db.Column(db.String(100), primary_key=True)
    public_id = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(100))
    admin = db.Column(db.Boolean)

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    
    if not data:
        return jsonify({'message': 'No data find, email and password needed ro register a user'}), 400

    try:
        if not re.fullmatch(regex_mail, data['email']):
            return jsonify({'message': 'You need to provide a valid email'})
    except KeyError:
        return jsonify({'message': 'You need to provide an email'})

    try:
        if data['password'] == '':
            return jsonify({'message': 'You need to provide a compliant password'})
    except KeyError:
        return jsonify({'message': 'You need to provide a password'})

    # Check if there is a password and the username is an email
    hashed_password = generate_password_hash(data['password'], method='sha256')
    public_id = str(uuid.uuid4())
    new_user = User(email=data['email'], public_id=public_id, name=public_id, password=hashed_password, admin=False)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User has been created!'}), 201

if __name__ == "__main__":
    app.run(debug=True)