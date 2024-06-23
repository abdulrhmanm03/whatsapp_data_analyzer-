from fastapi import APIRouter, UploadFile, Response, HTTPException
from fastapi.responses import JSONResponse
from src.utils.utils import file_to_pd_frame
from src.utils.Data_holder import data_holder
from src.utils.session import create_session_token


router = APIRouter(prefix="/upload_file")


@router.post("/")
async def upload_file(file: UploadFile, response: Response):
    
    try:
        contents = await file.read()
        decoded_file = contents.decode('utf-8')
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Failed to read or decode file: {e}")
    
    df = file_to_pd_frame(decoded_file)
    if df.empty:
        return JSONResponse(status_code=422, content={"error": "Failed to load file"})
    
    data_holder.name = file.filename
    data_holder.df = df
    
    session_token = create_session_token(file.filename)
    response.set_cookie(key="token", value=session_token, httponly=True)
    
    return {"filename": file.filename}