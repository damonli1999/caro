from flask import Blueprint, request, jsonify, render_template,redirect
from helpers import token_required
from models import db, User, Contact, contact_schema, contacts_schema

api = Blueprint('api',__name__, url_prefix='/api')

@api.route('/cars', methods = ['POST'])
@token_required
def create_car(current_user_token):
    make = request.json['make']
    model = request.json['model']
    year = request.json['year']
    mileage = request.json['mileage']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    car = Contact(make, model, year, mileage, user_token = user_token )

    db.session.add(car)
    db.session.commit()

    response = contact_schema.dump(car)
    return jsonify(response)

@api.route('/cars', methods = ['GET'])
@token_required
def get_contact(current_user_token):
    a_car = current_user_token.token
    contacts = Contact.query.filter_by(user_token = a_car).all()
    response = contacts_schema.dump(contacts)
    return jsonify(response)

@api.route('/cars/<id>', methods = ['GET'])
@token_required
def get_single_car(current_user_token, id):
    contact = Contact.query.get(id)
    response = contact_schema.dump(contact)
    return jsonify(response)

@api.route('/cars/<id>', methods = ['POST','PUT'])
@token_required
def update_car(current_user_token,id):
    contact = Contact.query.get(id) 
    contact.make = request.json['make']
    contact.model = request.json['model']
    contact.year = request.json['year']
    contact.mileage = request.json['mileage']
    contact.user_token = current_user_token.token

    db.session.commit()
    response = contact_schema.dump(contact)
    return jsonify(response)

@api.route('/cars/<id>', methods = ['DELETE'])
@token_required
def delete_car(current_user_token, id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    response = contact_schema.dump(contact)
    return jsonify(response)