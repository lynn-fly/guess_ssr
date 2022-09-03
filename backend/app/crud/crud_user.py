from typing import Optional
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from sqlalchemy import Column,and_
from app.models import User
from app.crud.base import CRUDBase
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import get_password_hash, verify_password


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):

    def get_by_username(self, db: Session, *, username: str) -> Optional[User]:
        return db.query(User).filter(User.username == username).first()

    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        db_obj = User(
            username=obj_in.username,
            hashed_password=get_password_hash(obj_in.password),
            is_admin=obj_in.is_admin,
            email=obj_in.email,
            nick_name = obj_in.nick_name,
            dept_name = obj_in.dept,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def bulk_save(self,db:Session,*, objs:[UserCreate]) :
        userlist = [User(
            username=obj.username,
            hashed_password=get_password_hash(obj.password),
            email=obj.email,
            nick_name = obj.nick_name,
            dept_name = obj.dept,
            ) for obj in objs]
        db.bulk_save_objects(userlist)
        db.commit()

    # 高效的方式
    # fourth_time = datetime.utcnow()
    # db.session.execute(
    #     User.__table__.insert(),
    #     [{"username": 'Execute NAME ' + str(i), "password": password} for i in range(10000)]
    # )
    # db.session.commit()
    # five_time = datetime.utcnow()
    # print((five_time - fourth_time).total_seconds())



    def update(
            self, db: Session, *, db_obj: User, obj_in: UserUpdate
    ) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        if update_data.get('password'):
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password

        # obj_data = jsonable_encoder(db_obj)
        obj_data = db_obj.as_dict()
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def authenticate(self, db: Session, *, username: str, password: str) -> Optional[User]:
        user = self.get_by_username(db, username=username)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    def get_uploads(self, db: Session, *, filters=None,
            order_by: Column = None,
            page: int = 1,
            limit: int = 10):
        query = db.query(
            self.model.id, self.model.nick_name, self.model.upload_file_url,self.model.upload_comment,self.model.thumbed
        )
        offset = limit * (page - 1)
        if filters is not None:
            query = query.filter(*filters)
            #query = query.filter(and_(User.upload_heart_value==50))
        if order_by is not None:
            query = query.order_by(order_by)
        query = query.offset(offset).limit(limit)
        return [r._asdict() for r in query.all()]
    
    # 获取中奖人员列表
    def get_results(self, db: Session, *, filters=None,
            order_by: Column = None,
            page: int = 1,
            limit: int = 10):
        query = db.query(
            self.model.username, self.model.nick_name, self.model.dept_name,self.model.first_prize_level,self.model.second_prize_level
        )
        offset = limit * (page - 1)
        if filters is not None:
            query = query.filter(*filters)
            #query = query.filter(and_(User.upload_heart_value==50))
        if order_by is not None:
            query = query.order_by(order_by)
        query = query.offset(offset).limit(limit)
        return [r._asdict() for r in query.all()]




user = CRUDUser(User)


