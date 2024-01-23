from fastapi import APIRouter, HTTPException

text2imgs_router = APIRouter(prefix="/text2img", tags=["text2img"])