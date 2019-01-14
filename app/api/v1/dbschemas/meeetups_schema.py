from marshmallow import Schema, fields
from ..utils.validate import required

class MeetupSchema(Schema):
    """ This class represents meetups schema."""

    id = fields.Int(dump_only=True)
    createdOn = fields.DateTime(dump_only=True)
    location = fields.Str(required=True, validate=(required))
    images = fields.List(fields.Str(), required=False)
    topic = fields.Str(required=True, validate=(required))
    happeningOn = fields.Str(required=True, validate=(required))
    tags = fields.List(fields.Str(), required=False)
    