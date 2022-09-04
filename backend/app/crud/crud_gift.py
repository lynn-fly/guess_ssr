
from typing import Optional
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from sqlalchemy import Column,and_
from app.models import Gift
from app.crud.base import CRUDBase
from app.schemas.gift import GiftCreate, GiftUpdate
from app.core.security import get_password_hash, verify_password

class CRUDGift(CRUDBase[Gift, GiftCreate, GiftUpdate]):

    def reduceOneAllowance(
            self, db: Session, *, db_obj: Gift
    ) -> Gift:
        sql = f"update gift set allowance = allowance - 1 where id = {db_obj.id}"
        result = db.execute(sql)
        db.commit()
        db.refresh(db_obj)
        return db_obj
gift = CRUDGift(Gift)