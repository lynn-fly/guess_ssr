from fastapi import APIRouter

from app.api.api_v1.endpoint import login, posts, categories, attachments,user,hwmock


api_router = APIRouter()
api_router.include_router(login.router, tags=['login'])
api_router.include_router(posts.router, tags=['posts'], prefix='/posts')
api_router.include_router(categories.router, tags=['categories'], prefix='/categories')
api_router.include_router(attachments.router, tags=['attachments'], prefix='/attachments')
api_router.include_router(user.router, tags=['user'], prefix='/user')
api_router.include_router(hwmock.router, tags=['hw'], prefix='/v2.1')