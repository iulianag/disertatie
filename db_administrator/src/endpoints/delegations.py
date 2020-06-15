from fastapi import APIRouter
from fastapi import HTTPException

router = APIRouter()


@router.get("/delegations", tags=["delegations"])
async def get_delegations():
    return {"delegationname": "fakecurrentdelegation"}


@router.post("/delegations", tags=["delegations"])
async def post_delegation():
    return {"delegationname": "fakecurrentdelegation"}


@router.delete("/delegations", tags=["delegations"])
async def delete_delegation():
    return {"delegationname": "fakecurrentdelegation"}
