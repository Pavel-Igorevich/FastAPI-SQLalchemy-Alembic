import uuid
import shutil
from fastapi import APIRouter, UploadFile, HTTPException, status

from .utils import save_image_as_webp
from .exceptions import FileException


router = APIRouter(
    prefix="/files",
    tags=["Files"]
)


@router.post("/images")
async def load_image(file: UploadFile):
    # todo сделать pydantic форму с привязкой к таблице
    if file.content_type not in {"image/png", "image/jpeg"}:
        raise FileException.invalid_format()
    unique_filename = f"{uuid.uuid4()}.webp"
    save_image_as_webp(file.file, unique_filename)
    # todo сохранить фото с привязкой в бд
    return FileException.success_upload(unique_filename)

