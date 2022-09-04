from datetime import datetime
from sqlalchemy import Boolean, Integer, Column, String

from app.db.base import Base


class Gift(Base):
    id = Column(Integer, primary_key=True)
    is_active = Column(Boolean, default=True)
    name = Column(String(50), unique=True)
    pic_name = Column(String(50), unique=True)
    note = Column(String(128), default='')
    allowance = Column(Integer,default=0) #剩余数量
    level = Column(Integer,default=0) # 奖品等级


