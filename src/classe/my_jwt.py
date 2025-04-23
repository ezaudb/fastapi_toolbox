import jwt
import os
import datetime

from dotenv import load_dotenv

class MyJwt:
    def __init__(self):
        load_dotenv()
        self._secret_key = os.getenv("SECRET_KEY")
        self._token_expires_minutes = int(os.getenv("TOKEN_EXPIRES_MINUTES"))

    def encode(self):
        payload = {"exp": datetime.datetime.now() + datetime.timedelta(minutes=self._token_expires_minutes)}
        token = jwt.encode(payload, self._secret_key, algorithm="HS256")

        return token
    
    def decode(self, token):
        jwt.decode(token, self._secret_key, algorithms=["HS256"])