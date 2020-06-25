import jwt
from jwt.exceptions import InvalidSignatureError, DecodeError


def create_token(data, secret):

    token = jwt.encode(data, secret, algorithm='HS256')
    return token


def verify_signature(token):

    try:
        json = jwt.decode(token, "acelera", algorithms="HS256")
        return json
        
    except DecodeError:
        return {"error": 2}
    except InvalidSignatureError:
        return {"error": 2}