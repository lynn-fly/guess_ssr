
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
    ) -> bool:
        sql = f"update gift set allowance = allowance - 1 where id = {db_obj.id} and allowance > 0"
        result = db.execute(sql)
        #student = db.query(Gift).with_for_update(read=False, nowait=False).filter(Gift.id == db_obj.id, Gift.allowance > 0).one()
        #student.allowance -= 1
        #student2 = db.query(Gift).filter(Gift.id == db_obj.id, Gift.allowance > 0).update({"allowance": student.allowance})
        # old_gift = db.query(Gift).with_for_update().get(db_obj.id)
        # result  = db.query(Gift.allowance).with_for_update().filter_by(id=db_obj.id).first()
        # allowance = result[0]
        # allowance -= 1
        # old_gift.allowance = allowance
        if result.rowcount < 1:
            print("============================")
        db.flush()
        #db.commit()
        #db.refresh(db_obj)

        return result.rowcount >= 1
gift = CRUDGift(Gift)