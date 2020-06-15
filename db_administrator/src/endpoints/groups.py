from fastapi import APIRouter
from fastapi import HTTPException

router = APIRouter()


@router.get("/groups", tags=["groups"])
async def get_groups():
    return {"groupname": "fakecurrentgroup"}


@router.post("/groups", tags=["groups"])
async def post_group():
    return {"groupname": "fakecurrentgroup"}


@router.get("/groups/{group_id}", tags=["groups"])
async def get_group(group_id: int):
    return {"groupname": "fakecurrentgroup"}


@router.delete("/groups/{group_id}", tags=["groups"])
async def delete_group(group_id: int):
    return {"groupname": "fakecurrentgroup"}


@router.put("/groups/{group_id}", tags=["groups"])
async def put_group(group_id: int):
    return {"groupname": "fakecurrentgroup"}