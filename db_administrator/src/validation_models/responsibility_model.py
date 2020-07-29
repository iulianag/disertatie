from pydantic import BaseModel


class ResponsibilityIn(BaseModel):
    profile_id: int
    group_id: int