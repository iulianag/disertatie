from fastapi import APIRouter
from fastapi import HTTPException

router = APIRouter()


@router.get("/types", tags=["types"])
async def get_types():
    return {"typename": "fakecurrenttype"}


@router.post("/types", tags=["types"])
async def post_type():
    return {"typename": "fakecurrenttype"}


@router.get("/types/{type_id}", tags=["types"])
async def get_type(type_id: int):
    return {"typename": "fakecurrenttype"}


@router.delete("/types/{type_id}", tags=["types"])
async def delete_type(type_id: int):
    return {"typename": "fakecurrenttype"}


@router.put("/types/{type_id}", tags=["types"])
async def put_type(type_id: int):
    return {"typename": "fakecurrenttype"}