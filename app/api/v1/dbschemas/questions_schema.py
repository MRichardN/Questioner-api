from marshmallow import Schema, fields
from ..utils.validate import required

class QuestionSchema(Schema):
    """ This question represents question schema """

    id = fields.Int(dump_only=True)
    createdOn = fields.DateTime(dump_only=True)
    createdBy = fields.Int(required=True)
    meetup = fields.Int(required=True)
    title = fields.Str(required=False, validate=(required))
    body = fields.Str(required=True, validate=(required))
    votes = fields.Int(dump_only=True)
    
    