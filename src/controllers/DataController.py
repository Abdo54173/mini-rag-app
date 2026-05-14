from .BaseController import BaseController
from fastapi import APIRouter ,FastAPI ,Depends ,UploadFile

class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.size_scale =1048576 # convert megabytes to bytes 

    def validate_uploaded_file(self ,file: UploadFile):
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False ,"file type not allowed"

        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale:
            return False ,"file size exceeds limit"

        return True ,"file is valid"