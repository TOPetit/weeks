from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import re
import uuid
import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

regex_mail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

app = Flask(__name__)
CORS(app)

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
        # check if the email match the email regex
        if not re.fullmatch(regex_mail, data['email']):
            return jsonify({'message': 'You need to provide a valid email'})
    except KeyError:
        return jsonify({'message': 'You need to provide an email'})

    try:
        if data['password'] == '':
            return jsonify({'message': 'You need to provide a compliant password'})
    except KeyError:
        return jsonify({'message': 'You need to provide a password'})

    user = User.query.filter_by(email=data['email']).first()

    if user:
        return jsonify({'message': 'This user already exists'})

    hashed_password = generate_password_hash(data['password'], method='sha256')
    public_id = str(uuid.uuid4())
    new_user = User(email=data['email'], public_id=public_id, name=public_id, password=hashed_password, admin=False)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User has been created!'}), 201

@app.route('/login', methods=['POST'])
def login():
    auth = request.json

    if auth and auth['email'] and auth['password']:
        user = User.query.filter_by(email=auth['email']).first()
        if user:
            #check password
            if check_password_hash(user.password, auth['password']):
                token = jwt.encode({'public_id': user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
                return jsonify({'token': token})
            return jsonify({'message': 'Could not login'}), 401
        return jsonify({'message': 'Could not login'}), 401

    return jsonify({'message': 'Could not login'}), 401

@app.route('/users')
def list_users():
    users = User.query.all()
    output = []
    for user in users:
        user_data = {}
        user_data['email'] = user.email
        user_data['public_id'] = user.public_id
        user_data['name'] = user.name
        user_data['password'] = user.password
        user_data['admin'] = user.admin
        output.append(user_data)
    return jsonify({'users': output})

@app.route('/user/<string:public_id>')
def get_user(public_id):
    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message': 'Could not find this user.'})

    user_data = {}
    user_data['email'] = user.email
    user_data['public_id'] = user.public_id
    user_data['name'] = user.name
    user_data['password'] = user.password
    user_data['admin'] = user.admin

    return jsonify({'user': user_data})

@app.route('/delete/<string:public_id>', methods=['DELETE'])
def delete_user(public_id):
    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message': 'Could not find this user.'})

    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'This user has been deleted.'})

@app.route('/user/name/<string:public_id>', methods=['PUT'])
def set_name(public_id):
    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message': 'Could not find this user.'}), 400
    
    try:
        data = request.json
    except:
        return jsonify('message', 'Data is missing.'), 400

    try:
        user.name = data['name']
        db.session.commit()
        return jsonify({'message': 'Name modified'})
    except:
        return jsonify({'message': 'Could not modify the name of this user.'}), 400

if __name__ == "__main__":
    app.run(debug=True)