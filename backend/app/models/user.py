from datetime import datetime
from sqlalchemy import Boolean, Integer, Column, String, ForeignKey,Text,LargeBinary
from sqlalchemy.orm import relationship
from app.db.base import Base


class User(Base):
    id = Column(Integer, primary_key=True)
    is_active = Column(Boolean, default=True)
    timestamp = Column(Integer, default=lambda: int(datetime.timestamp(datetime.utcnow())), index=True)
    is_admin = Column(Boolean, default=False)
    is_local = Column(Boolean, default=True)
    username = Column(String(16), unique=True)
    mobile_number  = Column(String(16))
    dept_name   = Column(String(50))
    nick_name = Column(String(50))
    hashed_password = Column(String(254))
    email = Column(String(128), unique=True, index=True)
    heart_value = Column(Integer,default=0)
    answer_heart_value  = Column(Integer,default=0)
    upload_heart_value   = Column(Integer,default=0)
    lottery_count    = Column(Integer,default=0)
    is_prize  = Column(Boolean, default=False)
    first_prize_level  =  Column(Integer,default=0) # 第一次抽奖获取几等奖
    first_prize_time   =  Column(Integer,default=0) # 第一次抽奖获奖时间
    second_prize_level  =  Column(Integer,default=0)
    second_prize_time   =  Column(Integer,default=0)
    answerids  = Column(String(128),default='-1') #答对题目的id（1，2，3，4）
    upload_file_url = Column(String(128),default='')
    upload_file = Column(LargeBinary) #二进制保存上传的图片
    upload_comment  = Column(String(128),default='')
    upload_time = Column(Integer,default=0) # Javascript 获取时间 new Date(1661991352 * 1000) 这个是UTC时间根据时区自己转换
    thumbed  = Column(Text,default='-1') # 保存点赞人的id，如“1，2，3”
    # gift_id = Column(Integer, ForeignKey('gift.id'))
    # gift = relationship('Gift', back_populates='gifts')
