from datetime import datetime
from sqlalchemy import Boolean, Integer, Column, String,Text

from app.db.base import Base


class Riddle(Base):
    id = Column(Integer, primary_key=True)
    is_active = Column(Boolean, default=True)
    name = Column(String(60), unique=True)
    question = Column(Text)
    answer = Column(String(128))
    point = Column(Integer,default=0)