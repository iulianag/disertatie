from fastapi import APIRouter
from fastapi import HTTPException

router = APIRouter()


@router.get("/profiles", tags=["profiles"])
async def get_profiles():
    return {"profilename": "fakecurrentprofile"}


@router.post("/profiles", tags=["profiles"])
async def post_profile():
    return {"profilename": "fakecurrentprofile"}


@router.get("/profiles/{profile_id}", tags=["profiles"])
async def get_profile(profile_id: int):
    return {"profilename": "fakecurrentprofile"}


@router.delete("/profiles/{profile_id}", tags=["profiles"])
async def delete_profile(profile_id: int):
    return {"profilename": "fakecurrentprofile"}


@router.put("/profiles/{profile_id}", tags=["profiles"])
async def put_profile(profile_id: int):
    return {"profilename": "fakecurrentprofile"}