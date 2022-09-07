from typing import Any
from datetime import timedelta
from sqlalchemy.orm import Session
import re
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse

from app import schemas, crud, models
from app.api import deps
from app.core.config import settings
from app.core import security

router = APIRouter()


@router.post('/login/access-token', response_model=schemas.Token, status_code=status.HTTP_201_CREATED)
def login_access_token(
        db: Session = Depends(deps.get_db),
        form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """OAuth2 compatible token login, get an access token for future requests"""
    user = crud.user.authenticate(
        db=db,
        username=form_data.username,
        password=form_data.password
    )
    if not user:
        raise HTTPException(
            status_code=400, detail="Incorrect admin username or password"
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        'access_token': security.create_access_token(
            user.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer"
    }

@router.post('/login/user', response_model=Any, status_code=status.HTTP_201_CREATED)
def login_user(db: Session = Depends(deps.get_db), *, ulogin: schemas.UserLogin) -> Any:
     user = crud.user.get_by_username(db=db,username=ulogin.username)
     db_nick_name =  re.sub(r"\s+", "", user.nick_name).lower()
     input_nick_name = re.sub(r"\s+", "", ulogin.nick_name).lower()
     if not user or db_nick_name != input_nick_name:
        raise HTTPException(
            status_code=400, detail="姓名和工号匹配错误！"
        )
     access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
     return {
        'access_token': security.create_access_token(
            user.id, expires_delta=access_token_expires
        ),
        'userId':user.id,
        'userName':user.nick_name,
        'heartValue':user.heart_value,
        'isAnswerMax': user.answer_heart_value == 50,
        'isUpload': user.upload_heart_value == 50,
        'lotteryCount': user.lottery_count,
        'isLocal':user.is_local,
        'answeredIds':user.answeredids.split(','),
    }


@router.get('/login/info')
def login_info(
        current_user: models.User = Depends(deps.get_current_user),
):
    data = {
        "roles": ['admin'] if current_user.is_admin else [],
        'userId':current_user.id,
        'userName':current_user.nick_name,
        'heartValue':current_user.heart_value,
        'isAnswerMax': current_user.answer_heart_value == 50,
        'isUpload': current_user.upload_heart_value == 50,
        'lotteryCount': current_user.lottery_count,
        'isLocal':current_user.is_local,
        'answeredIds':current_user.answeredids.split(','),
    }
    return JSONResponse(content=jsonable_encoder(data), status_code=status.HTTP_200_OK)

