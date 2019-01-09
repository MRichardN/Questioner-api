import datetime
from flask import Blueprint, request, jsonify, abort, make_response 
from app.api.v1.models.questions_model import Question
from app.api.v1.models.meetups_model import Meetup
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

@version1.route('/question/<int:question_id>/downvote/', methods=["PATCH"])
def downvote_question(question_id):
    """
    downvote a question.
    """
    if not request.json:
          abort(400)
    if 'title' in request.json and type(request.json['title']) != str:
         abort(400)
    if 'body' in request.json and type(request.json['body']) is not str:
        abort(400)
    this_question = [this_question for this_question in question_list if this_question["id"]==question_id]
    if this_question:
        title = request.json.get('title', this_question[0]["title"])
        body = request.json.get('body', this_question[0]['body'])
        createdOn = datetime.datetime.now()
        createdBy = request.json.get('createdBy', this_question[0]['createdBy'])
        meetup = request.json.get('meetup', this_question[0]['meetup'])
        votes = request.json.get('votes', this_question[0]['votes']) -1
        updated_question = question.update_question(question_id, title, body, createdOn, createdBy, meetup, votes)
        return jsonify({ 'status':201, 'data': updated_question}), 201
    abort(404)

@version1.route('/question/<int:question_id>/upvote/', methods=["PATCH"])
def upvote_question(question_id):
    """
    upvote a question.
    """
    if not request.json:
          abort(400)
    if 'title' in request.json and type(request.json['title']) != str:
         abort(400)
    if 'body' in request.json and type(request.json['body']) is not str:
        abort(400)
    this_question = [this_question for this_question in question_list if this_question["id"]==question_id]
    if this_question:
        title = request.json.get('title', this_question[0]["title"])
        body = request.json.get('body', this_question[0]['body'])
        createdOn = datetime.datetime.now()
        createdBy = request.json.get('createdBy', this_question[0]['createdBy'])
        meetup = request.json.get('meetup', this_question[0]['meetup'])
        votes = request.json.get('votes', this_question[0]['votes'] ) +1
        updated_question = question.update_question(question_id, title, body, createdOn, createdBy, meetup, votes)
        return jsonify({ 'status':201, 'data': updated_question}), 201
    abort(404)  
   

@version1.route('/meetups/<int:meetup_id>/', methods=['GET','POST','PUT','DELETE'])
def get_a_specific_meetup(meetup_id):
    """
    Get a specific question.
    """
    if request.method == 'GET':
        mitup_list = meetup.show_meetups()
        mtup = [mtup for mtup in mitup_list if mtup["id"] == meetup_id]
        return jsonify({ 'status': 200, 'data': mtup}), 200
    abort(404) 

@version1.route('/post_question/', methods=["POST"])
def post_question():
    """
    Post a question.
    """
    if not request.json or not 'title' in request.json:
        abort(400)
    post_quiz = {
    'id': meetup_list[-1]['id'] + 1,
    'title': request.json['title'],
    'body': request.json['body'],
    'createdOn': datetime.datetime.now(),
    "createdBy" :request.json['createdBy'],
    'meetup' : request.json['meetup'],
    "votes": request.json['votes']
    }
    question.add_question(post_quiz)
    return jsonify({ 'status': 201, 'data': post_quiz, }), 201      

@version1.route('/meetups/<int:meetup_id>/rsvp/', methods=["POST"])
def post_rsvp(meetup_id):
    """
    Post a rsvp.
    """
    if not request.json or not 'meetup' in request.json:
        abort(400)
    post_rsvps = {
    'id': meetup_list[-1]['id'] + 1,
    'meetup': request.json['meetup'],
    'user': request.json['user'],
    "response" :request.json['response']
    }

    rsvp.add_rsvp(post_rsvps)
    return jsonify({ 'status': 201, 'data': post_rsvps, }), 201 
