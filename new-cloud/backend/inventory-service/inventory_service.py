from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__) 
api = Api(app=app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@DB2:5432/inventory_db'
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productName = db.Column(db.String(200), nullable=False)
    price = db.Column(db.String(15), nullable=False)
    description = db.Column(db.String(40), nullable=False)

    def __init__(self, productName, price, description, password):
        self.productName = productName
        self.price = price
        self.description= description

    
class ProductServices(Resource):
    def get(self, description):
        product = Product.query.filter_by(description=description)
        if product:
            product_data = {
                'id': product.id,
                'productName': product.productName,
                'price': product.price,
                'description': product.description,
            }
            return jsonify(product_data)
        return jsonify({'message': 'Error  product not found'}), 404

    def post(self, productName, description, password, price):
        data = request.get_json()
        product = Product(productName=data.get('productName'), description=data.get('description'), price=data.get('price'))
        if not product.productName or not product.description or not product.password:
            return jsonify({"message": "Error product data is missing"}), 404
        
        db.session.add(product)
        db.session.commit()
        return jsonify(message='product created successfully'), 201
    
    def put(self):
        data = request.json
        description = data.get('description')
        product = Product.query.filter_by(description)
        if not product:
            return jsonify(message='product not found'), 404
        
        if data['productName']:
            product.productName = data['productName']
        if data['password']:
            product.password = data['password']
        if data['price']:
            product.price = data['price']
        if data['description']:
            product.description = data['description']
        db.session.commit()
        return jsonify(message='product data updated successfully')
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)