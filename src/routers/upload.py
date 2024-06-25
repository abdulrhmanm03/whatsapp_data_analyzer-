from fastapi import APIRouter, UploadFile, Cookie, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from src.utils.utils import file_to_pd_frame
from typing import Optional
from src.db.crud import get_current_user_id, create_user_df
from src.db.database import get_db



router = APIRouter(prefix="/upload_file")


@router.post("/")
async def upload_file(file: UploadFile,
                      token: Optional[str] = Cookie(None),
                      db: Session = Depends(get_db)):
    if not token:
        raise HTTPException(status_code=401, detail="Authentication required: sign up or log in.")
     
    user_id = get_current_user_id(token=token, db=db)
    if not user_id:
        raise HTTPException(status_code=401, detail="Authentication required: sign up or log in.")
    
    try:
        contents = await file.read()
        decoded_file = contents.decode('utf-8')
    except Exception:
        raise HTTPException(status_code=422, detail=f"Failed to read file")
    
    df = file_to_pd_frame(decoded_file)
    if df.empty:
        return JSONResponse(status_code=422, content={"error": "Failed to load file"})
    
    df_json = df.to_json()
    df_item = {
               "title": file.filename,
               "df_json": df_json
               }
    
    try:
        file_id = create_user_df(db=db, item=df_item, user_id=user_id).id
    except Exception:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: Failed to save DataFrame. Error")
    
    return {"file_id": file_id}