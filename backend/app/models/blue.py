from datetime import datetime
from sqlalchemy import Boolean, Integer, Column, String, ForeignKey,Text,LargeBinary

from app.db.base import Base


class Blue(Base):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,default=0)
    upload_file_url = Column(String(128),default='')
    upload_comment  = Column(String(255),default='')
    upload_time = Column(Integer, default=lambda: int(datetime.timestamp(datetime.utcnow())), index=True)
    thumbed  = Column(Text,default='-1') # 保存点赞人的id，如“1，2，3”
    thumbe_times   =  Column(Integer,default=0)