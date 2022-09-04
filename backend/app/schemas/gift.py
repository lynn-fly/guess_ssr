from typing import Optional
from pydantic import BaseModel


class GiftBase(BaseModel):
    pass


class GiftCreate(GiftBase):
    name: str
    allowance:Optional[int]
    level:Optional[int]


class GiftUpdate(GiftBase):
    allowance:Optional[int]