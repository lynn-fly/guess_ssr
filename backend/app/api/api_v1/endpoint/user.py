import random
import base64
import shutil
import uuid

from datetime import datetime
from typing import Any
from sqlalchemy.orm import Session
from sqlalchemy import desc,and_,or_
from fastapi import APIRouter, Depends, HTTPException, status,UploadFile, File, Form
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app import crud, schemas
from app.utils import utils
from app.api import deps
from app.models import User



router = APIRouter()

@router.post('/save_answer/{ans_id}',dependencies=[Depends(deps.get_current_user)], response_model=Any, status_code=status.HTTP_201_CREATED)
def save_answer(db: Session = Depends(deps.get_db),user: User = Depends(deps.get_current_user),*,ans_id: str) -> Any:
     
     if not user:
        raise HTTPException(
            status_code=400, detail="user not found"
        )
     answerids = user.answerids.split(',')
     answer_heart_value = user.answer_heart_value
     heart_value = user.heart_value
     lottery_count = user.lottery_count
     if(answer_heart_value < 50 and not ans_id in answerids):
        answer_heart_value += 10
        heart_value += 10
        answerids.append(ans_id)
        if answer_heart_value>=50:
            lottery_count += 1
     
     
     
     new_answerids = ','.join(answerids)
     obj_u = schemas.UserUpdate(
        answer_heart_value=answer_heart_value,
        heart_value =heart_value,
        answerids = new_answerids,
        lottery_count = lottery_count
        )
     new_user = crud.user.update(db,db_obj=user,obj_in=obj_u)
     return {
        'userId':user.id,
        'userName':user.nick_name,
        'heartValue':new_user.heart_value,
        'lotteryCount ':new_user.lottery_count,
        'answerId': new_user.answerids.split(',')
    }

#saveThumbed
@router.post('/save_thumbed/{user_id}',dependencies=[Depends(deps.get_current_user)], response_model=Any, status_code=status.HTTP_201_CREATED)
def save_answer(db: Session = Depends(deps.get_db),user: User = Depends(deps.get_current_user),*,user_id:int) -> Any:
     if not user:
        raise HTTPException(
            status_code=400, detail="user not found"
        )
     thumbed_user = crud.user.get(db,id=user_id)
     if not thumbed_user:
        raise HTTPException(
            status_code=400, detail="thumbed user not found"
        )
     thumbeds = thumbed_user.thumbed.split(',')
     if(not str(user.id) in thumbeds):
        thumbeds.append(str(user.id))

     new_thumbeds= ','.join(thumbeds)
     obj_u = schemas.UserUpdate(
        thumbed=new_thumbeds,
        )
     new_user = crud.user.update(db,db_obj=thumbed_user,obj_in=obj_u)
     return {
        'thumbedUserId':new_user.id,
        'thumbedUserName':new_user.nick_name,
        'thumbeUsers': new_user.thumbed.split(',')
    }

@router.post('/get_prize',dependencies=[Depends(deps.get_current_user)], response_model=Any, status_code=status.HTTP_201_CREATED)
def get_prize(db: Session = Depends(deps.get_db),user: User = Depends(deps.get_current_user)) -> Any:
    if not user:
        raise HTTPException(
            status_code=400, detail="user not found"
        )
    lottery_count = user.lottery_count
    first_prize_time = user.first_prize_time
    second_prize_time = user.second_prize_time
    first_prize_level = user.first_prize_level
    second_prize_level = user.second_prize_level
    
    if lottery_count < 1:
        raise HTTPException(
            status_code=500, detail="lottery count is 0"
        )
    if second_prize_time > 0 and first_prize_time > 0:
        raise HTTPException(
            status_code=500, detail="you had prize towice"
        )
    gifts = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,9]
    index=random.sample(range(0,len(gifts)-1),1)
    giftlevel = gifts[index[0]]
    if first_prize_time == 0:
        first_prize_time = int(datetime.timestamp(datetime.utcnow()))
        first_prize_level = giftlevel
    else:
        second_prize_time = int(datetime.timestamp(datetime.utcnow()))
        second_prize_level = giftlevel

    obj_u = schemas.UserUpdate(
        first_prize_time=first_prize_time,
        first_prize_level=first_prize_level,
        second_prize_time=second_prize_time,
        second_prize_level=second_prize_level,
        lottery_count = lottery_count - 1,
        is_prize = True
        )
    new_user = crud.user.update(db,db_obj=user,obj_in=obj_u)
    return {
        'userId':new_user.id,
        'lotteryNumber':giftlevel,
    }

@router.post('/save_upload',
             dependencies=[Depends(deps.get_current_user)], 
             response_model=Any, status_code=status.HTTP_201_CREATED)
def save_upload(
        db: Session = Depends(deps.get_db), 
        user: User = Depends(deps.get_current_user),
        upload_file: UploadFile = File(...), comment: str = Form(...)) -> Any:
    if not user:
        raise HTTPException(
            status_code=400, detail="user not found"
        )
    upload_heart_value = user.upload_heart_value
    lottery_count = user.lottery_count
    heart_value = user.heart_value
    if (upload_heart_value > 0):
        raise HTTPException(
            status_code=500, detail="uploaded yet"
        )
    upload_heart_value = 50
    lottery_count += 1
    heart_value += 50
    ext = upload_file.filename.split('.')[-1]
    u_name = uuid.uuid4()
    file_location = f"uploads/{u_name}.{ext}"
    
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(upload_file.file, file_object)
    user_up = schemas.UserUpdate(
        upload_heart_value=upload_heart_value,heart_value=heart_value,lottery_count=lottery_count,
        upload_comment=comment,upload_file_url=f"/upload/{u_name}.{ext}",upload_time=int(datetime.timestamp(datetime.utcnow()))
    )
    new_user = crud.user.update(db,db_obj=user,obj_in=user_up)
    return {
        'userId':new_user.id,
        'userName':new_user.nick_name,
        'heartValue':new_user.heart_value,
        'lotteryCount ':new_user.lottery_count,
        'fileUrl':new_user.upload_file_url,
        'comment':new_user.upload_comment,
        'uploadTime':new_user.upload_time
    }

@router.get('/upload_list',
             dependencies=[Depends(deps.get_current_user)], 
             response_model=Any, status_code=status.HTTP_200_OK)
def upload_list(
        db: Session = Depends(deps.get_db), 
        user: User = Depends(deps.get_current_user),*,page: int = 1, limit: int = 10) -> Any:
    filters = (and_(User.upload_heart_value==50),) # 逗号不能少，如果只有一个条件的时候
    order_by =desc(User.upload_time)
    data = crud.user.get_uploads(db,order_by=order_by,filters=filters,page=page,limit=limit)
    return JSONResponse(content=data, status_code=status.HTTP_200_OK)