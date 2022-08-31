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
    nss_city_file = "uuuu.csv"
    with open(nss_city_file,'r',newline='',encoding='utf-8-sig') as csvfile:
        csv_reader = csv.reader(csvfile)
        birth_header = next(csv_reader)
        emps = []
        
        for row in csv_reader:
            print(row)
            user_in = schemas.UserCreate(
                username=row[1], 
                password = '123456',
                dept = row[3], 
                is_admin=False,
                nick_name = row[2],
                email=f'{row[1]}@qq.com'
                )
            crud.user.create(db, obj_in=user_in)
            print(f'Done {row[1]}')
            #emps.append(user_in)
        #crud.user.bulk_save(db, objs=emps)


