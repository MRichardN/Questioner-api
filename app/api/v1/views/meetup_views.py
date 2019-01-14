# third party import
from flask import jsonify, request, abort, make_response
from marshmallow import ValidationError

# local import
from app.api.v1 import version1
from ..dbschemas.meeetups_schema import MeetupSchema
from ..models.meetups_model import Meetup



MEETUPS = Meetup()

@version1.route('/meetups/upcoming/', methods=['GET'])
def get_all_meetups():
    """ View all meetups."""
    meetups = MEETUPS.getAll()
    data = MeetupSchema(many=True).dump(meetups)
    return jsonify({'status': 200, 'result': data}), 200

    

@version1.route('/post_meetup/', methods=['POST'])
def post_meetups():
    """ Post a meetup."""
    data = request.get_json()

    # No data provided
    if not data:
        abort(make_response(jsonify({'status': 400, 'error': 'Failed: No data provided'}), 400))

    try:    
        # Check if request is valid
        data = MeetupSchema().load(data)
        
    # display errors alongside valid data entered
    except ValidationError as errors:
        errors.messages
        valid_data = errors.valid_data
        abort(make_response(jsonify({'status': 400, 'error' : 'Invalid data. Please enter all required fields', 'errors': errors.messages, 'valid_data':valid_data}), 400))    

    # Save meetup 
    new_meetup = MEETUPS.save(data)
    result = MeetupSchema().dump(new_meetup)
    return jsonify({'status': 201, 'message': 'Meetup created', 'data': [result]}), 201   
    
 
@version1.route('/meetups/<int:meetup_id>/', methods=['GET'])
def get_a_specific_meetup(meetup_id):
    """ Get a specific question."""

    #check if meetup exists
    if not MEETUPS.exists('id', meetup_id):
        abort(make_response(jsonify({'status': 404, 'error': 'Meetup does not exist'}), 404))
    
    # Get a specific meetup
    meetup = MEETUPS.getOne('id', meetup_id)
    result = MeetupSchema().dump(meetup)
    return jsonify({'status':200, 'data': result}), 200


@version1.route('/meetups/<int:meetup_id>/<string:rsvps>/', methods=['POST'])
def rspvs_meetup(meetup_id, rsvps):
    """ rsvp meetup."""
    response = ['yes', 'no', 'maybe']

    # Check if meetup exists
    if not MEETUPS.exists('id', meetup_id):
        abort(make_response(jsonify({'status': 404, 'message': 'Meetup does not exist'}), 404))

    # Check if rsvp is valid
    if rsvps not in response:
        abort(make_response(jsonify({'status': 400, 'message': 'Invalid rsvp'}), 400))

    meetup = MEETUPS.getOne('id', meetup_id)
    return jsonify({
        'status': 200,
        'message': 'Responded successfully',
        'data': {
            'meetup': meetup['id'],
            'topic' : meetup['topic'],
            'status': rsvps
        }
    }), 200
    
