from fastapi import APIRouter, UploadFile
from .models.model_pipeline import model_pipeline
import io
from PIL import Image

img2text_router = APIRouter(prefix="/img2text", tags=["img2text"])

@img2text_router.post("/askimg")
async def askimg(text: str, image: UploadFile):
    content = image.file.read()
    image = Image.open(io.BytesIO(content))
    result = model_pipeline(text, image)
    return {"answer": result}
