
# Third party import
from flask import jsonify, request, abort, make_response
from marshmallow import ValidationError
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required,
                             get_jwt_identity, jwt_refresh_token_required, get_raw_jwt, JWTManager)

# local import
from app.api.v1 import version1
from ..models.token_model import RevokedTokenModel
from ..dbschemas.users_schema import UserSchema
from ..models.users_model import User

usr = User()


@version1.route('/register/', methods=['POST'])
def register_user():
    """ Register user endpoint."""
    data = request.get_json()

    
    # Empty entry
    if not data:
        abort(make_response(jsonify({'status': 400, 'message': 'No data provided'}), 400))
    try:
            
        # Check if request is valid
        data = UserSchema().load(data)
        
        #display errors and valid data entered
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

@version1.route('/login/', methods=['POST'])
def login():
    """ Login a registered user"""
    data = request.get_json()

    # Check for empty entries
    if not data:
        abort(make_response(jsonify({'status': 400, 'message': 'No data provided'}), 400))

    # Check if credentials have been passed

    try:
        username = data['username']
        password = data['password']
    except:
        abort(make_response(jsonify({'status': 400, 'message': 'Invalid credentials'}), 400))
    

    # Check if username exists
    if not usr.exists('username', username):
        abort(make_response(jsonify({'status': 404, 'message' : 'User not found'}), 404))

    user = usr.getOne('username', username)

    # Check if password match
    if not usr.checkpasswordhash(user['password'], password):
        abort(make_response(jsonify({'status': 404, 'message' : 'Invalid password'}), 404))

     # Generate user tokens 
    access_token = create_access_token(identity=user['id'], fresh=True)
    refresh_token = create_refresh_token(identity=True)
    return jsonify({
        'status': 200, 
        'message': 'User logged in successfully',
        'access_token': access_token,
        'refresh_token': refresh_token
        }), 200

@version1.route('/refresh_token/', methods=['POST'])
@jwt_refresh_token_required
def refresh_token():
    """ Refresh user token."""
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)
    return jsonify({'status': 200, 'message': 'Token refreshed successfully', 'access_token': access_token})

# Endpoint for revoking the current users access token
# @version1.route('/logout', methods=['DELETE'])
# @jwt_required
# def logout():
#     blacklisted_token =[]
#     jti = get_raw_jwt()['jti']
#     blacklisted_token.append(jti)
#     return jsonify({"msg": "Successfully logged out"}), 200



@version1.route('/logout/', methods=['DELETE'])
@jwt_required
def logout():
    """ Logout user """
    jti = get_raw_jwt()['jti']
    RevokedTokenModel().add(jti)
    return jsonify({'status': 200, 'message': 'Logged out successfully'}), 200
    

# Endpoint for revoking the current users access token
# @version1.route('/logout', methods=['DELETE'])
# @jwt_required
# def logout():
#     jti = get_raw_jwt()['jti']
#     blacklist.add(jti)
#     return jsonify({"msg": "Successfully logged out"}), 200    


'''

@version1.route('/protected', methods=['GET'])
@jwt_required
def protected():
    username = get_jwt_identity()
    return jsonify(logged_in_as=username), 200       
'''






