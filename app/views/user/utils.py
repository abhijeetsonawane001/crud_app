import json

from itsdangerous import BadTimeSignature, URLSafeTimedSerializer

serializer = URLSafeTimedSerializer("secret-key")


def generate_verification_token(data):
    """ It generates a email verification token """

    token = serializer.dumps(json.dumps(data))

    return token


def verify_verification_token(token, expires_in=86400):
    try:
        return json.loads(serializer.loads(token, expires_in))
    except BadTimeSignature:
        return "Verification Token Expired"
