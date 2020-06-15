from fastapi import APIRouter, Depends
from src.dependencies.authorization import is_authenticated

router = APIRouter()


@router.get("/users",
            tags=["Users"])
async def get_users(user_id=Depends(is_authenticated)):
    return {"username": user_id}


@router.post("/users", tags=["Users"])
async def post_user():
    return {"username": "fakecurrentuser"}


@router.get("/users/{id}", tags=["Users"])
async def get_user(id: int):
    return {"username": "fakecurrentuser"}


@router.delete("/users/{id}", tags=["Users"])
async def delete_user(id: int):
    return {"username": "fakecurrentuser"}


@router.put("/users/{id}", tags=["Users"])
async def put_user(id: int):
    return {"username": "fakecurrentuser"}