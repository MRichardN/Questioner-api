# third party import
from marshmallow import Schema, fields

# local import
from ..utils.validate import email, required, password

class UserSchema(Schema):
    """  Class for user schema """

    id = fields.Int(dump_only=True)
    firstname = fields.Str(required=True, validate=(required))
    lastname = fields.Str(required=True, validate=(required))
    othername = fields.Str(required=False)
    username = fields.Str(required=True, validate=(required))
    phoneNumber = fields.Str(required=True, validate=(required))
    email = fields.Email(required=True, validate=(email))
    password = fields.Str(required=True, validate=(password))
    registeredOn = fields.DateTime(dump_only=True)
    isAdmin = fields.Bool(dump_only=True)
