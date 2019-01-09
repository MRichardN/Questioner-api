import datetime
from flask import Blueprint, request, jsonify, abort, make_response 
from app.api.v1.models.questions_model import Question
from app.api.v1.models.meetup_model import Meetup
from app.api.v1.models.rsvp_model import Rsvp
from app.api.v1.models import question_list, user_list, meetup_list, rsvp_list


version1 = Blueprint("version1", __name__, url_prefix='/api/v1')

question = Question(question_list)
meetup = Meetup(meetup_list)
rsvp = Rsvp(rsvp_list)


@version1.errorhandler(404)
def item_not_found(error):
    """
    Custom response to 404 errors.
    """
    return make_response(jsonify({ 'status' :404, 'error ' : 'Failed: Item not found'}), 404)


@version1.errorhandler(400)
def bad_method(error):
    """
    Custom response to 400 errors.
    """
    return make_response(jsonify({ 'status':400, 'error': 'Failed: bad request'}))

@version1.route('/meetups/upcoming/', methods=["GET", "POST"])
def get_all_meetups():
    """
    View all meetups.
    """
    if meetup:
        return jsonify({'status':200, 'data': meetup.show_meetups()}), 200
    abort(404)

@version1.route('/post_meetup/', methods=["POST"])
def post_meetups():
    """
    Post a meetup.
    """
    if not request.json or not 'topic' in request.json:
        abort(400)
    post_mtup = {
    'id': question_list[-1]['id'] + 1,
    'createdOn': request.json['createdOn'],
    "location" : request.json['location'],
    "topic" : request.json['topic'],
    "happeningOn" : request.json['happeningOn']
    }
    meetup.add_meetup(post_mtup)
    return jsonify({ 'status': 201, 'data': post_mtup, }), 201 