

from marshmallow import ValidationError
from flask import  request, jsonify, make_response, abort

# local imports
from app.api.v2 import version2
from app.api.v1.models.questions_model import Question
from app.api.v1.dbschemas.questions_schema import QuestionSchema



QUESTION = Question()

@version2.route('/post_question/', methods=["POST"])
def post_question():
    """ Post a question."""
    data = request.get_json()


    # No data provied
    if not data:
        abort(make_response(jsonify({'status': 400, 'message': 'No data sent'}), 400))

    # Check if request is valid
    try:
        data = QuestionSchema().load(data)
        # return errors alongside valid data
    except ValidationError as errors:
        errors.messages
        valid_data = errors.valid_data
        abort(make_response(jsonify({'status': 400, 'error' : 'Invalid data. Please enter all fields', 'errors': errors.messages, 'valid_data':valid_data}), 400)) 

    # Save question and return response
    question = QUESTION.save(data)
    result = QuestionSchema().dump(question)
    return jsonify({'status': 201, 'Success': 'Question created successfully', 'data': result}), 201


   

@version2.route('/question/<int:question_id>/downvote/', methods=["PATCH"])
def downvote_question(question_id):
    """ Downvote a question."""

    # check if question exists
    if not QUESTION.exists('id', question_id):
        abort(make_response(jsonify({'status': 404, 'error': 'Question not found'}), 404))

    # Downvote the question
    question = QUESTION.downvote(question_id)
    result = QuestionSchema().dump(question)
    return jsonify({'status': 200, 'message': 'Quesion down-voted', 'data': result}), 200
    

@version2.route('/question/<int:question_id>/upvote/', methods=["PATCH"])
def upvote_question(question_id):
    """ upvote a question."""

    # check if question exists
    if not QUESTION.exists('id', question_id):
        abort(make_response(jsonify({'status': 404, 'error': 'Question not found'} ),404))

    # Downvote the question
    question = QUESTION.upvote(question_id)
    result = QuestionSchema().dump(question)
    return jsonify({'status': 200, 'message': 'Quesion up-voted', 'data': result}), 200

      

