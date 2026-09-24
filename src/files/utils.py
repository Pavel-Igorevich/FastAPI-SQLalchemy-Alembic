from PIL import Image
from fastapi import UploadFile

from .exceptions import FileException


def save_image_as_webp(image_file: UploadFile, file_name: str):
    try:
        image = Image.open(image_file)
        image.save(f"./static/images/{file_name}", "webp")
    except Exception:
        raise FileException.processing_failed()
