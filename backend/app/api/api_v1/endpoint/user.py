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