from fastapi import APIRouter, UploadFile, File

from controllers.file import file_upload_controller

router = APIRouter(
    prefix="/file",
    tags=["file"]
)


@router.post("/")
def get_file(image: UploadFile = File(...)):
    return file_upload_controller(image)
