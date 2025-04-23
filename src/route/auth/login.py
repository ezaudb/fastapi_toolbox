from fastapi import APIRouter
from service.auth.auth_service import AuthService

router = APIRouter()

@router.post("/auth/login", tags=["public"])
async def auth_login():
    auth_service = AuthService()
    return await auth_service.get_token()