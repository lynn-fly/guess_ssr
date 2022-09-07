from functools import reduce
from itertools import count
from math import fabs
import random
import base64
import shutil
import uuid
import xlwt
import os
from PIL import Image
from io import BytesIO
from datetime import datetime
from typing import Any
from sqlalchemy.orm import Session
from sqlalchemy import desc,and_,or_
from fastapi import APIRouter, Depends, HTTPException, status,UploadFile, File, Form
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse,StreamingResponse

from app import crud, schemas
from app.utils import utils
from app.api import deps
from app.models import User,Blue



router = APIRouter()

@router.post('/save_answer/{ans_id}/{is_ok}',dependencies=[Depends(deps.get_current_user)], response_model=Any, status_code=status.HTTP_201_CREATED)
def save_answer(db: Session = Depends(deps.get_db),user: User = Depends(deps.get_current_user),*,ans_id: str,is_ok: int) -> Any:
     
     if not user:
        raise HTTPException(
            status_code=400, detail="用户不存在"
        )
     answerids = user.answerids.split(',')
     answeredids = user.answeredids.split(',')
     answer_heart_value = user.answer_heart_value
     heart_value = user.heart_value
     lottery_count = user.lottery_count
     
     if(ans_id in answeredids or ans_id in answerids):
        raise HTTPException(
            status_code=500, detail="曾经回答过的问题无论对错已经是曾经了！"
        )

     if(answer_heart_value < 50 and not ans_id in answerids and is_ok == 1):
        answer_heart_value += 10
        heart_value += 10
        answerids.append(ans_id)
        if answer_heart_value>=50:
            lottery_count += 1
     
     if(not ans_id in answeredids):
        answeredids.append(ans_id)
        
     new_answerids = ','.join(answerids)
     new_answeredids = ','.join(answeredids)
     obj_u = schemas.UserUpdate(
        answer_heart_value=answer_heart_value,
        heart_value =heart_value,
        answerids = new_answerids,
        answeredids = new_answeredids,
        lottery_count = lottery_count
        )
     new_user = crud.user.update(db,db_obj=user,obj_in=obj_u)
     return {
        'userId':user.id,
        'userName':user.nick_name,
        'heartValue':new_user.heart_value,
        'lotteryCount':new_user.lottery_count,
        'answerId': new_user.answerids.split(','),
        'answeredIds':new_user.answeredids.split(','),
    }

#saveThumbed
@router.post('/save_thumbed/{blue_id}',dependencies=[Depends(deps.get_current_user)], response_model=Any, status_code=status.HTTP_201_CREATED)
def save_thumbed(db: Session = Depends(deps.get_db),user: User = Depends(deps.get_current_user),*,blue_id:int) -> Any:
     if not user:
        raise HTTPException(
            status_code=400, detail="用户不存在"
        )
     thumbed_blue = crud.blue.get(db,id=blue_id)
     if not thumbed_blue:
        raise HTTPException(
            status_code=400, detail="内容不存在"
        )
     thumbeds = thumbed_blue.thumbed.split(',')
     thumbe_times = thumbed_blue.thumbe_times
     if(not str(user.id) in thumbeds):
        thumbeds.append(str(user.id))
        thumbe_times += 1
     new_thumbeds= ','.join(thumbeds)
     obj_u = schemas.BlueUpdate(
        thumbed=new_thumbeds,
        thumbe_times=thumbe_times
        )
     new_blue = crud.blue.update(db,db_obj=thumbed_blue,obj_in=obj_u)
     return {
        'thumbedUserId':user.id,
        'thumbedUserName':user.nick_name,
        'thumbeUsers': new_blue.thumbed.split(','),
        'thumbeTimes':new_blue.thumbe_times
    }

@router.post('/get_prize',dependencies=[Depends(deps.get_current_user)], response_model=Any, status_code=status.HTTP_200_OK)
def get_prize(db: Session = Depends(deps.get_db),user: User = Depends(deps.get_current_user)) -> Any:
#@router.post('/get_prize', response_model=Any, status_code=status.HTTP_200_OK)
#def get_prize(db: Session = Depends(deps.get_db)) -> Any:
    # for test  start
    #randomUserId =random.sample(range(2,1912),1)
    #user = crud.user.get(db,id=randomUserId)
    # fot test end
    # if not access_user:
    #     raise HTTPException(
    #         status_code=400, detail="user not found"
    #     )
    user_updated = False
    #second_count = crud.user.get_second(db)
    with db.begin(subtransactions=True):
        # user = None
        # try:
        #     user = crud.user.locke_user(db,db_obj=access_user)
        # except Exception as e:
        #     print(f"抽奖异常:{e.__str__()}")
        if not user:
            raise HTTPException(
                status_code=400, detail="用户不存在"
            )
        lottery_count = user.lottery_count
        first_prize_time = user.first_prize_time
        second_prize_time = user.second_prize_time
        first_prize_level = user.first_prize_level
        second_prize_level = user.second_prize_level

        if lottery_count < 1:
            raise HTTPException(
                status_code=500, detail="抽奖次数不足"
            )
        if second_prize_time > 0 and first_prize_time > 0:
            raise HTTPException(
                status_code=500, detail="已经抽奖两次啦"
            )
        gifts = [1,2,2,3,3,3,4,4,4,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,9,9,9,9,9,9,9,9,9
        ,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]
        # 如果第一次已经抽取了，就在三等奖和四等奖中抽取，且中间总额不能大于总数量 -  总人数
        has_gifts = True
        if first_prize_level > 0:      
            #if second_count <= 150:
            #    gifts = [6,7,8,9,10,10,10,10,10,10,10,10,10,10,10,10,10]
            # else:
            #     has_gifts = False
            gifts = [9,9,9,9,9,9,9,9,9]
        random.shuffle(gifts)
        giftlevel = -1
        retry = 30
        while giftlevel == -1 and retry > 0 and has_gifts:
            index=random.sample(range(0,len(gifts)-1),1)
            giftlevel = gifts[index[0]]
            
            gift = crud.gift.get(db,id=giftlevel)
            if (gift and gift.allowance > 0 ):
                upOK =  crud.gift.reduceOneAllowance(db,db_obj=gift)
                if (not upOK):
                    giftlevel = -1
            else:
                giftlevel = -1
            retry -= 1
        
        #if retry < 1 or giftlevel == 10:
        if retry < 1:
            giftlevel = 9

        now_time = int(datetime.timestamp(datetime.utcnow()))
        user_updated = crud.user.update_giftlevel(db,db_obj=user,now_time=now_time,gift_level=giftlevel)
    if user_updated:
        db.commit()
        db.refresh(user)
        return {
            'userId':user.id,
            'lotteryCount':user.lottery_count,
            'lotteryNumber':giftlevel,
            'heartValue':user.heart_value,
        }
    else:
        db.rollback()
        print("user update false")
        raise HTTPException(
                status_code=500, detail="两次抽奖次数已经用完"
            )
    
            
            

@router.post('/save_upload',
             dependencies=[Depends(deps.get_current_user)], 
             response_model=Any, status_code=status.HTTP_201_CREATED)
def save_upload(
        db: Session = Depends(deps.get_db), 
        user: User = Depends(deps.get_current_user),
        upload_file: UploadFile = File(...), comment: str = Form(...)) -> Any:
    if not user:
        raise HTTPException(
            status_code=400, detail="用户不存在"
        )
    
    ext = upload_file.filename.split('.')[-1]
    u_name = uuid.uuid4()
    file_location = f"uploads/{u_name}.{ext}"
    context_type = upload_file.content_type
    allow_types = ['image/jpeg', 'image/jpg', 'image/png','jpeg','jpg','png']
    if context_type not in allow_types:
        raise HTTPException(
            status_code=500, detail="文件类型不支持，请上传jpeg/jpg/png格式图片"
        )
    
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(upload_file.file, file_object)
    
    img_file_size = os.path.getsize(file_location)/1000/1000
    if img_file_size >= 5:
        raise HTTPException(
            status_code=500, detail="上传图片不能大于5M"
        )
    if img_file_size < 1:
        img_file_size = 1
    file_location_c = f"uploads/{u_name}_c.{ext}"
    try:
        
        sImg=Image.open(file_location)
        w,h=sImg.size
        dImg=sImg.resize((int(w/img_file_size),int(h/img_file_size)),Image.ANTIALIAS)  
        dImg.save(file_location_c) 
        #print (file_location_c +" successful.")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"图片处理异常，{e.__str__()}"
        )
    
    blue_in = schemas.BlueCreate(user_id=user.id, upload_comment=comment,upload_file_url=f"/upload/{u_name}_c.{ext}")
    new_blue = crud.blue.create(db, obj_in=blue_in)
    
    upload_heart_value = user.upload_heart_value
    lottery_count = user.lottery_count
    heart_value = user.heart_value
    if (upload_heart_value > 0 or lottery_count > 1):
        return {
        'userId':user.id,
        'userName':user.nick_name,
        'heartValue':user.heart_value,
        'lotteryCount':user.lottery_count,
        'fileUrl':user.upload_file_url,
        'comment':user.upload_comment,
        'uploadTime':user.upload_time,
        'isFirst':False
    }

    upload_heart_value = 50
    lottery_count += 1
    heart_value += 50
    

    user_up = schemas.UserUpdate(
        upload_heart_value=upload_heart_value,heart_value=heart_value,lottery_count=lottery_count,
    )
    new_user = crud.user.update(db,db_obj=user,obj_in=user_up)
    return {
        'userId':new_user.id,
        'userName':new_user.nick_name,
        'heartValue':new_user.heart_value,
        'lotteryCount':new_user.lottery_count,
        'fileUrl':new_user.upload_file_url,
        'comment':new_user.upload_comment,
        'uploadTime':new_user.upload_time,
        'isFirst':True
    }

@router.get('/upload_list',
             dependencies=[Depends(deps.get_current_user)], 
             response_model=Any, status_code=status.HTTP_200_OK)
def upload_list(
        db: Session = Depends(deps.get_db), 
        user: User = Depends(deps.get_current_user),*,page: int = 1, limit: int = 12,isFirst:bool = False) -> Any:
    
    uids = crud.blue.get_uploaded_uids(db)
    ids = [u["id"] for u in uids]
    if len(ids) > 12:
        if isFirst:
            max = ids[-4:]
            max.reverse()
            max.extend(random.sample(ids[0:-4], 8) )
            print(max)
            ids = max
            print(ids)
        else:
            ids = random.sample(ids, 12)
    else:
        ids.reverse()
    filters = (and_(Blue.id.in_(tuple(ids))),) # 逗号不能少，如果只有一个条件的时候
    order_by =desc(Blue.thumbe_times)
    data = crud.blue.get_uploads(db,order_by=order_by,filters=filters,page=page,limit=limit)
    return JSONResponse(content=data, status_code=status.HTTP_200_OK)

@router.post('/result',
             dependencies=[Depends(deps.get_current_active_admin)], 
             response_model=Any, status_code=status.HTTP_200_OK)
def get_results(
        db: Session = Depends(deps.get_db), *,searchKey: str = Form(''), gift:int =Form(...), page: int = 1, limit: int = 2500) -> Any:
    filters = [] #  如果是 tuple逗号不能少，如果只有一个条件的时候
    if (searchKey) :
        filters.append(or_(User.username.like(f'%{searchKey}%'),User.nick_name.like(f'%{searchKey}%')))
    if(gift > 0) :
        filters.append(or_(User.first_prize_level == gift, User.second_prize_level == gift)) # 逗号不能少，如果只有一个条件的时候
    else:
        filters.append(or_(User.first_prize_level > 0, User.second_prize_level > 0)) # 逗号不能少，如果只有一个条件的时候
    filters = tuple(filters)
    order_by = User.username
    data = crud.user.get_results(db,order_by=order_by,filters=filters,page=page,limit=limit)
    return JSONResponse(content=data, status_code=status.HTTP_200_OK)

@router.post('/export',dependencies=[Depends(deps.get_current_active_admin)], response_model=Any, status_code=status.HTTP_200_OK)
def fl_query(db: Session = Depends(deps.get_db), *,searchKey: str = Form(''), gift:int =Form(...), page: int = 1, limit: int = 2500):
     header = ['工号', '姓名', '部门', "奖品一", "奖品二"]
     """
     以流的形式导出到excel     """
 
     def set_style():
         """
         设置样式
         :return:
         """
         # 居中设置
         alignment = xlwt.Alignment()
         alignment.horz = xlwt.Alignment.HORZ_CENTER
         alignment.vert = xlwt.Alignment.VERT_CENTER
 
         # 设置表头字体样式
         head_style = xlwt.XFStyle()
         font = xlwt.Font()
         font.name = 'Times New Roman'  # 字体
         font.bold = True  # 字体加粗
         head_style.font = font  # 设置字体
         head_style.alignment = alignment  # Add Alignment to Style
 
         # 设置表中内容样式
         cont_style = xlwt.XFStyle()
         font = xlwt.Font()
         font.name = 'Times New Roman'  # 字体
         font.bold = False  # 字体加粗
         cont_style.font = font  # 设置字体
         cont_style.alignment = alignment  # Add Alignment to Style
 
         # 设置单元格边界
         borders = xlwt.Borders()
         borders.left = xlwt.Borders.THIN
         borders.right = xlwt.Borders.THIN
         borders.top = xlwt.Borders.THIN
         borders.bottom = xlwt.Borders.THIN
         head_style.borders = borders
         cont_style.borders = borders
         return head_style, cont_style
 
     def get_sheet(_book, _index):
         """
         创建sheet页
         :param _book:
         :param _index:
         :return:
         """
         _name = "sheet_{}".format(str(_index))
         _sheet = _book.add_sheet(_name)
         return _sheet
 
     def write_head(_head, _sheet, _head_style):
         """
         写入表头
         :param _head:
         :param _sheet:
         :param _head_style:
         :return:
         """
         for head in range(len(header)):
             context = str(header[head])
             need_width = (1 + len(context)) * 556 * 2
             table_sheet.col(head).width = need_width
             # table_sheet.write(0, head, context, style=_head_style)
             table_sheet.write(0, head, context, style=_head_style)
 
     sheet_index = 1
     book = xlwt.Workbook(encoding='utf-8')  # 创建 Excel 文件
     table_sheet = get_sheet(book, sheet_index)  # 添加sheet表
     h_style, c_style = set_style()
     write_head(header, table_sheet, h_style)
 
     # 获取数据
     filters = [] #  如果是 tuple逗号不能少，如果只有一个条件的时候
     if (searchKey) :
        filters.append(or_(User.username.like(f'%{searchKey}%'),User.nick_name.like(f'%{searchKey}%')))
     if(gift > 0) :
        filters.append(or_(User.first_prize_level == gift, User.second_prize_level == gift)) # 逗号不能少，如果只有一个条件的时候
     else:
        filters.append(or_(User.first_prize_level > 0, User.second_prize_level > 0)) # 逗号不能少，如果只有一个条件的时候
     filters = tuple(filters)
     order_by = User.username
     fls = crud.user.get_results(db,order_by=order_by,filters=filters,page=page,limit=limit)
     # 插入数据
     row = 1
     gifts = ['未中奖','AVATR户外座椅-灰','AVATR定制保温杯','AVATR城市画展系列T恤衫',
      'AVATR户外折叠整理箱-灰','AVATR户外超声波防潮野餐地垫-灰','AVATR环保束口包','AVATR精品帆布包','AVATR杜邦电脑包','E值']
     for f_log in fls:
         table_sheet.write(row, 0, str(f_log['username']), style=c_style)
         table_sheet.write(row, 1, str(f_log['nick_name']), style=c_style)
         table_sheet.write(row, 2, str(f_log['dept_name']), style=c_style)
         table_sheet.write(row, 3, str(gifts[f_log['first_prize_level']]) if f_log['first_prize_level'] > 0 else '--', style=c_style) 
         table_sheet.write(row, 4, str(gifts[f_log['second_prize_level']]) if f_log['second_prize_level'] > 0 else '--', style=c_style)          
         row += 1
         if row > 50000:  # 单表数量超过 65535 条 添加新的表
             row = 1
             sheet_index += 1
             table_sheet = get_sheet(book, sheet_index)  # 添加sheet表
             write_head(header, table_sheet, h_style)
     sio = BytesIO()  # 返回文件流到浏览端下载，浏览端必须以form提交方式方能下载成功！
     book.save(sio)  # 这点很重要，传给save函数的不是保存文件名，而是一个StringIO流
     sio.seek(0)  # 保存流
     # 组装header
     headers = {"content-type": "application/vnd.ms-excel", "content-disposition": 'attachment;filename=download.xls'}
     # 以流的形式返回浏览器
     return StreamingResponse(sio, media_type="xls/xlsx", headers=headers)