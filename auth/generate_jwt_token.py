import os

import jwt

# Secret key to encode and decode the JWT
SECRET_KEY = os.getenv("JWT_SECRET")

# Payload data
payload = {
    "user_id": 1,
    "username": "andreas daiminger",
    # 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token expiry set to 1 hour
}

encoded_jwt = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
print(f"Encoded JWT: {encoded_jwt}")

# Optionally, decode to check the content
decoded_payload = jwt.decode(encoded_jwt, SECRET_KEY, algorithms=["HS256"])
print(f"Decoded JWT: {decoded_payload}")
