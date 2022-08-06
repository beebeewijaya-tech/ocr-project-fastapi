from fastapi import UploadFile

import shutil
import pytesseract


def image_to_text(file: UploadFile):
    file_path = "txtFile"

    with open(file_path, "w+b") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return pytesseract.image_to_string(file_path, lang="eng")
