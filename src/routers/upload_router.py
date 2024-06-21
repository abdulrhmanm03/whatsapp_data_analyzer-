from fastapi import APIRouter, UploadFile
from fastapi.responses import JSONResponse
from src.utils.utils import file_to_pd_frame
from ..utils.Data_holder import data_holder


router = APIRouter(prefix="/upload_file")


@router.post("/")
async def upload_file(file: UploadFile):
    
    contents = await file.read()
    decoded_file = contents.decode('utf-8')
    
    df = file_to_pd_frame(decoded_file)
    if df.empty:
        return JSONResponse(status_code=422, content={"error": "Failed to load file"})
    
    data_holder.df = df
    
    return {"filename": file.filename}