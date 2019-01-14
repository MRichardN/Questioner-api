
import re
from marshmallow import ValidationError

def password(pwd):
    """ check password meets requirements."""
    if len(pwd) not in range(6, 13):
        raise ValidationError('password must be between 6 and 12 characters')

    if not re.search('[a-z]',pwd):
        raise ValidationError('password must atleast have a lower case character')

    if not re.search('[A-Z]', pwd):
        raise ValidationError('password must contain an upper case letter') 

    if not re.search('[0-9]', pwd):
        raise ValidationError('password must contain a numeric character') 


def email(value):
    """ check email format."""
    if not re.match(r"(^[a-zA-z0-9_.]+@[a-zA-z0-9-]+\.[a-z]+$)", value):
        raise ValidationError('Invalid email format')
    return value

def required(value):
    """Check a field does not contain null entries."""

    if isinstance(value, str):
        if not value.strip(' '):
            raise ValidationError('This parameter cannot be null')
        return value
    elif value:
        return value



      




   
        