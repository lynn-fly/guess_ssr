import random
from datetime import datetime
from typing import Any
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
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