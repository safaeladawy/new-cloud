from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) 
api = Api(app=app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@DB1:5432/accounts_db'
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(15), nullable=True, unique=True)
    email = db.Column(db.String(40), nullable=False, unique=True)
    password = db.Column(db.String(15), nullable=False, unique=False)

    def __init__(self, userName, phone, email, password):
        self.userName = userName
        self.phone = phone
        self.email= email
        self.password = password

    
class UsersServices(Resource):
    def get(self, username, password):
        user = User.query.filter_by(userName=username).filter_by(password=password)
        if user:
            user_data = {
                'id': user.id,
                'userName': user.userName,
                'phone': user.phone,
            }

            return jsonify(user_data)
        return jsonify({'message': 'Error user not found'}), 404

    def post(self, userName, email, password, phone):
        data = request.get_json()
        user = User(userName=data.get('userName'), email=data.get('email'), password=data.get('password'), phone=data.get('phone'))
        if not user.userName or not user.email or not user.password:
            return jsonify({"message": "Error User data is missing"}), 404
        try:
            db.session.add(user)
        except:
            return jsonify({"message": 'user data email or password are repeated'}), 404
        db.session.commit()
        return jsonify(message='user created successfully'), 201
    
    def put(self):
        data = request.json
        email = data.get('email')
        user = User.query.filter_by(email)
        if not user:
            return jsonify(message='user not found'), 404
        
        if data['userName']:
            user.userName = data['userName']
        if data['password']:
            user.password = data['password']
        if data['phone']:
            user.phone = data['phone']
        if data['email']:
            user.email = data['email']
        db.session.commit()
        return jsonify(message='user data updated successfully')        

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)