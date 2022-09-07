from numbers import Integral
from typing import Optional
from pydantic import BaseModel


class BlueBase(BaseModel):
    pass

class BlueCreate(BlueBase):
    user_id: int
    upload_file_url : str
    upload_comment  : str


class BlueUpdate(BlueBase):
    thumbed  : Optional[str]
    thumbe_times:Optional[int]