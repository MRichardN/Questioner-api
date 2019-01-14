# Third party import
from flask import jsonify, request, abort, make_response
from marshmallow import ValidationError
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required,
                             get_jwt_identity, jwt_refresh_token_required, get_raw_jwt)

# local import
from app.api.v1 import version1
from ..dbschemas.users_schema import UserSchema
from ..models.users_model import User

usr = User()


@version1.route('/register/', methods=['POST'])
def register_user():
    """ Register user endpoint."""
    data = request.get_json()

    
    # Empty data
    if not data:
        abort(make_response(jsonify({'status': 400, 'message': 'No data provided'}), 400))
    try:
            
        # Check if request is valid
        data = UserSchema().load(data)
        
        #display errors alongside valid data entered
    except ValidationError as errors:
        errors.messages
        valid_data = errors.valid_data
        abort(make_response(jsonify({'status': 400, 'message' : 'Invalid data. Please fill all required fields', 'errors': errors.messages, 'valid_data':valid_data}), 400))
    
    # Check if username exists
    if next(filter(lambda u: u['username'] == data['username'], usr.getAll()), None):
        abort(make_response(jsonify({'status': 409, 'message' : 'Username already exists'}), 409))

    # Check if email exists    
    if usr.exists('email', data['email']):
        abort(make_response(jsonify({'status': 409, 'message' : 'Email already exists'}), 409))

    # Save new user and get result
    new_user = usr.save(data)
    result = UserSchema(exclude=['password']).dump(new_user)

    # Generate access and refresh tokens and return response
    access_token = create_access_token(identity=new_user['id'], fresh=True)
    refresh_token = create_refresh_token(identity=new_user['id'])
    return jsonify({
        'status': 201, 
        'message' : 'New user created ', 
        'data': result, 
        'access_token' : access_token, 
        'refresh_token' : refresh_token
        }), 201