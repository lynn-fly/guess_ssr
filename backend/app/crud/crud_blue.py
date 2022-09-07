
from typing import Optional
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from sqlalchemy import Column,and_
from app.models import Blue
from app.crud.base import CRUDBase
from app.schemas.blue import BlueCreate, BlueUpdate

class CRUDBlue(CRUDBase[Blue, BlueCreate, BlueUpdate]):

    def reduceOneAllowance(
            self, db: Session, *, db_obj: Blue
    ) -> bool:
        sql = f"update gift set allowance = allowance - 1 where id = {db_obj.id} and allowance > 0"
        result = db.execute(sql)
        if result.rowcount < 1:
            print("============================")
        db.flush()
        #db.commit()
        #db.refresh(db_obj)

        return result.rowcount >= 1
    def get_uploaded_uids(self, db: Session):
        query = db.query(self.model.id)
        query = query.order_by(Blue.thumbe_times)
        return [r._asdict() for r in query.all()]

    def get_uploads(self, db: Session, *, filters=None,
            order_by: Column = None,
            page: int = 1,
            limit: int = 10):
        query = db.query(
            self.model.id, self.model.upload_file_url,self.model.upload_comment,self.model.thumbed,self.model.thumbe_times
        )
        offset = limit * (page - 1)
        if filters is not None:
            query = query.filter(*filters)
            #query = query.filter(and_(User.upload_heart_value==50))
        if order_by is not None:
            query = query.order_by(order_by)
        query = query.offset(offset).limit(limit)
        return [r._asdict() for r in query.all()]
blue = CRUDBlue(Blue)