from fastapi import APIRouter
from classe.my_jwt import MyJwt

class AuthService:
    async def get_token(self):
        my_jwt = MyJwt()
        token = my_jwt.encode()
        
        return {"message": token}        