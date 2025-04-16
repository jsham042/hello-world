import jwt
from datetime import datetime, timedelta
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError

# Secret key for JWT encoding and decoding. In production, use a more secure key and keep it secret.
SECRET_KEY = "your_secret_key_here"
ALGORITHM = "HS256"


def generate_token(user_id):
    """
    Generates a JWT token for an authenticated user.

    :param user_id: The unique identifier for the user.
    :return: A JWT token as a string.
    """
    payload = {
        "user_id": user_id,
        "exp": datetime.utcnow() + timedelta(days=1),  # Token expires in 1 day
        "iat": datetime.utcnow(),
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token


def verify_token(token):
    """
    Validates the provided JWT token.

    :param token: The JWT token to validate.
    :return: The payload if the token is valid, raises an exception if invalid.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except ExpiredSignatureError:
        raise ValueError("Token has expired")
    except InvalidTokenError:
        raise ValueError("Invalid token")


# Example usage
if __name__ == "__main__":
    user_id = "12345"
    token = generate_token(user_id)
    print(f"Generated Token: {token}")

    try:
        payload = verify_token(token)
        print(f"Token is valid. Payload: {payload}")
    except ValueError as e:
        print(f"Token validation error: {e}")
