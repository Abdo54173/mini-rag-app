from fastapi import APIRouter, Depends, UploadFile
from src.helpers.config import get_settings, Settings
from src.controllers import DataController

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=[ "data"]
)

@data_router.post("/upload/{project_id}")
async def upload_data(
    project_id: str,
    file: UploadFile,
    app_settings: Settings = Depends(get_settings)
):

    is_valid ,result_signal = DataController().validate_uploaded_file(file=file)

    return {"signal": result_signal}