from typing import Optional
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from sqlalchemy import Column,and_,or_
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

    def update_giftlevel(self, db: Session, *, db_obj: User, now_time: int, gift_level:int) -> bool:
        
        sql = f'''
        update user set second_prize_level = case when first_prize_time > 0 and second_prize_time = 0 then {gift_level} else second_prize_level end, 
        second_prize_time = case when first_prize_time > 0 and second_prize_time = 0 then {now_time} else second_prize_time end,
        first_prize_level = case when first_prize_time = 0 and second_prize_time = 0 then {gift_level} else first_prize_level end,
        first_prize_time = case when first_prize_time = 0 and second_prize_time = 0 then {now_time} else first_prize_time end,
        lottery_count = lottery_count - 1, heart_value = heart_value - 50, is_prize  = 1 
        where id = {db_obj.id} and (first_prize_time = 0 or second_prize_time = 0)'''
        result = db.execute(sql)

        #old_user = db.query(User).with_for_update(read=False, nowait=False).filter(User.id == db_obj.id).one()
        # db_obj.lottery_count -=   1
        # db_obj.is_prize = True
        # update = 0
        # if db_obj.first_prize_time == 0:
        #     update = db.query(User).filter(User.id == db_obj.id, User.first_prize_time == 0)\
        #         .update({"first_prize_level": gift_level,"first_prize_time":now_time,"lottery_count":db_obj.lottery_count,"is_prize":db_obj.is_prize})
            
        # else:
        #     update = db.query(User).filter(User.id == db_obj.id, User.first_prize_time > 0, User.second_prize_time ==0)\
        #         .update({"second_prize_level": gift_level,"second_prize_time":now_time,"lottery_count":db_obj.lottery_count,"is_prize":db_obj.is_prize})
        if result.rowcount < 1:
            print(f"用户:{db_obj.username} - {db_obj.nick_name}已经全部抽取！")
        db.flush()
        #db.commit()
        #db.refresh(db_obj)
        return result.rowcount > 0

    def update_upload(self, db: Session, *, db_obj: User) -> bool:
        sql = f'''
        update user set upload_heart_value = 50
        lottery_count = lottery_count + 1,
        is_prize  = 1
        where id = {db_obj.id} and lottery_count < 2 and upload_heart_value = 0 '''
        result = db.execute(sql)

        #old_user = db.query(User).with_for_update(read=False, nowait=False).filter(User.id == db_obj.id).one()
        # db_obj.lottery_count -=   1
        # db_obj.is_prize = True
        # update = 0
        # if db_obj.first_prize_time == 0:
        #     update = db.query(User).filter(User.id == db_obj.id, User.first_prize_time == 0)\
        #         .update({"first_prize_level": gift_level,"first_prize_time":now_time,"lottery_count":db_obj.lottery_count,"is_prize":db_obj.is_prize})
            
        # else:
        #     update = db.query(User).filter(User.id == db_obj.id, User.first_prize_time > 0, User.second_prize_time ==0)\
        #         .update({"second_prize_level": gift_level,"second_prize_time":now_time,"lottery_count":db_obj.lottery_count,"is_prize":db_obj.is_prize})
        if result.rowcount < 1:
            print(f"用户:{db_obj.username} - {db_obj.nick_name}已经全部抽取！")
        db.flush()
        #db.commit()
        #db.refresh(db_obj)
        return result.rowcount > 0

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
            self.model.id, self.model.nick_name, self.model.upload_file_url,self.model.upload_comment,self.model.thumbed,self.model.thumbe_times
        )
        offset = limit * (page - 1)
        if filters is not None:
            query = query.filter(*filters)
            #query = query.filter(and_(User.upload_heart_value==50))
        if order_by is not None:
            query = query.order_by(order_by)
        query = query.offset(offset).limit(limit)
        return [r._asdict() for r in query.all()]

    def get_uploaded_uids(self, db: Session):
        query = db.query(
            self.model.id
        )
        query = query.filter(and_(User.upload_heart_value==50))
        query = query.order_by(User.thumbe_times)
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
    
    # 获取二次抽中的人数    
    def get_second(self, db: Session) -> int:
        count = db.query(self.model.username).filter(User.second_prize_level.in_((6,7,8,9,))).count()
        return count

    def get_nodraw(self, db: Session) -> User:
        user = db.query(User).filter(or_(User.first_prize_time == 0,User.second_prize_time == 0)).first()
        return user
    
    def locke_user(self, db: Session,*,db_obj:User) -> User:
        old_user = db.query(User).with_for_update(read=False, nowait=True).filter(User.id == db_obj.id).one()
        return old_user



user = CRUDUser(User)


