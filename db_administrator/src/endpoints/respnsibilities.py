from fastapi import APIRouter
from fastapi import HTTPException

router = APIRouter()


@router.get("/responsibilities", tags=["responsibilities"])
async def get_responsibilities():
    return {"responsibilityname": "fakecurrentresponsibility"}


@router.post("/responsibilities", tags=["responsibilities"])
async def post_responsibility():
    return {"responsibilityname": "fakecurrentresponsibility"}


@router.delete("/responsibilities", tags=["responsibilities"])
async def delete_responsibility():
    return {"responsibilityname": "fakecurrentresponsibility"}
