from fastapi import APIRouter
from app.apis.todo import todo_router
from app.apis.img2text import img2text_router

apis_router = APIRouter(prefix="/apis", tags=["apis"])
apis_router.include_router(todo_router)
apis_router.include_router(img2text_router)