from pydantic import BaseModel


class DelegationIn(BaseModel):
    user_id: int
    profile_id: int