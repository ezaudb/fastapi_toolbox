from fastapi import APIRouter

router = APIRouter()

@router.get("/home/welcome")
async def home_welcome():
    return {"message": "Hello World"}