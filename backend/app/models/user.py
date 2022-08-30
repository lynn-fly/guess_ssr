from datetime import datetime
from sqlalchemy import Boolean, Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class User(Base):
    id = Column(Integer, primary_key=True)
    is_active = Column(Boolean, default=True)
    timestamp = Column(Integer, default=lambda: int(datetime.timestamp(datetime.utcnow())), index=True)
    is_admin = Column(Boolean, default=False)
    username = Column(String(16), unique=True)
    hashed_password = Column(String(254))
    email = Column(String(128), unique=True, index=True)
    points = Column(Integer,default=0)
    is_draw = Column(Boolean, default=False)
    draw_time = Column(Integer,default=0)
    gift_id = Column(Integer, ForeignKey('gift.id'))
    gift = relationship('Gift', back_populates='gifts')
