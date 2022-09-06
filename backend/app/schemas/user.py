from numbers import Integral
from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    pass


class UserCreate(UserBase):
    username: str
    password: str
    is_admin: Optional[bool]
    is_local: Optional[bool]
    email: str
    dept:str
    nick_name:Optional[str]


class UserUpdate(UserBase):
    password: Optional[str]
    email: Optional[str]
    heart_value : Optional[int]
    answer_heart_value  : Optional[int]
    upload_heart_value   : Optional[int]
    lottery_count    : Optional[int]
    is_prize   : Optional[bool]
    first_prize_level  : Optional[int]
    first_prize_time   : Optional[int]
    second_prize_level  : Optional[int]
    second_prize_time   : Optional[int]
    answerids  : Optional[str]
    answeredids: Optional[str]
    upload_file_url : Optional[str]
    upload_comment  : Optional[str]
    thumbed  : Optional[str]
    upload_file: Optional[bytes]
    upload_time:Optional[int]
    thumbe_times:Optional[int]
class UserLogin(UserBase):
    username: str
    nick_name:str






