from sqlalchemy.orm import Session
from app import crud, schemas
from app.core.config import settings
import csv

def init_db(db: Session) -> None:
    user = crud.user.get_by_username(db, username=settings.FIRST_ADMIN)
    if not user:
        user_in = schemas.UserCreate(
            username=settings.FIRST_ADMIN,
            password=settings.FIRST_ADMIN_PASSWORD,
            is_admin=True,
            dept = '',
            nick_name = '',
            email='test@qq.com'
        )
        crud.user.create(db, obj_in=user_in)
    nss_city_file = "u0906.csv"
    with open(nss_city_file,'r',newline='',encoding='utf-8-sig') as csvfile:
        csv_reader = csv.reader(csvfile)
        birth_header = next(csv_reader)
        emps = []
        
        for row in csv_reader:
            print(row)
            user_in = schemas.UserCreate(
                username=row[0], 
                password = '123456',
                dept = row[2], 
                is_admin=False,
                nick_name = row[1],
                is_local =  '中国' in row[3] ,
                email=f'{row[0]}@qq.com'
                )
            crud.user.create(db, obj_in=user_in)
            print(f'Done {row[1]}')
            #emps.append(user_in)
        #crud.user.bulk_save(db, objs=emps)


