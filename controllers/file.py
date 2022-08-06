from fastapi import UploadFile, File

from services.file import image_to_text


def file_upload_controller(file: UploadFile):
    return image_to_text(file)
