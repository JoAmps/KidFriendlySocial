import jwt
import datetime
import bcrypt

print(bcrypt.__version__)

expiry_minutes_access_tokens = 15


class AccessTokens:
    @staticmethod
    def generate_access_token(username, secret, authorize):
        try:
            payload = {
                "username": username,
                "exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(minutes=expiry_minutes_access_tokens),
                "iat": datetime.datetime.utcnow(),
                "admin": authorize,
            }
            return jwt.encode(payload, secret, algorithm="HS256")
        except Exception as e:
            return e

    @staticmethod
    def decode_access_token(encoded_jwt, secret):
        try:
            decoded = jwt.decode(encoded_jwt, secret, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return "Token Signature expired. Please log in again", 403
        except jwt.InvalidTokenError:
            return "Token invalid. Please log in again", 403
        return decoded, 200
