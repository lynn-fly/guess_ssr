# -*-coding:utf-8-*-
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.exceptions import RequestValidationError
from fastapi.exception_handlers import request_validation_exception_handler
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse

from app.core.config import settings
from app.api.api_v1.api import api_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f'{settings.API_V1_STR}/openapi.json'
)

# CORS
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# mount frontend static files
app.mount("/static", StaticFiles(directory="frontend/dist/static"), name="static")
app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get('/')
async def read_index():
    return FileResponse('frontend/dist/index.html')


@app.exception_handler(404)
async def not_found(request: Request, exc):
    accept = request.headers.get('accept')
    if exc.status_code == 404 and 'text/html' in accept:
        return FileResponse('frontend/dist/index.html')
    else:
        return JSONResponse(content={'error': "Not found"}, status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    print(request)
    print('Validation Exception', exc)
    return await request_validation_exception_handler(request, exc)


if __name__ == '__main__':
    import uvicorn

    # dev
    uvicorn.run(f'{__name__}:app', port=5000, host='127.0.0.1', reload=True)
    # prod
    # uvicorn.run(app, port=80, host='0.0.0.0', log_config=settings.LOGGING)
