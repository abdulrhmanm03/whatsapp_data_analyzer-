from fastapi import APIRouter, HTTPException, Depends, Cookie
from src.utils.utils import encode_fig
from src.utils.plots import time_plot, pie_plot
from typing import Optional
import pandas as pd
from src.db.crud import get_current_user_id, get_df_item
from src.db.database import get_db
from sqlalchemy.orm import Session


router = APIRouter(prefix="/plots")



@router.get("/time_plot/")
async def send_time_plot(df_id: int,
                        db: Session = Depends(get_db),
                        token: Optional[str] = Cookie(None)):
    
    if not token:
        raise HTTPException(status_code=401, detail="Authentication required: sign up or log in.")
    if not df_id:
        raise HTTPException(status_code=400, detail="File ID is required.")
    df_item = get_df_item(db=db, id=df_id)
    if not df_item:
        raise HTTPException(status_code=404, detail="File not found.")
    user_id = get_current_user_id(token=token, db=db)
    if user_id != df_item.owner_id:
        raise HTTPException(status_code=403, detail="Forbidden: You do not have permission to access this DataFrame.") 
    df_json = df_item.df_json
    df = pd.read_json(df_json)
    
    time_plot_fig = time_plot(df) 
    encoded_fig = encode_fig(time_plot_fig)
    
    return {"Time plot": encoded_fig}



@router.get("/pie_plot/")
async def send_pie_plot(df_id: int,
                        db: Session = Depends(get_db),
                        token: Optional[str] = Cookie(None)):
            
    if not token:
        raise HTTPException(status_code=401, detail="Authentication required: sign up or log in.")
    if not df_id:
        raise HTTPException(status_code=400, detail="File ID is required.")
    df_item = get_df_item(db=db, id=df_id)
    if not df_item:
        raise HTTPException(status_code=404, detail="File not found.")
    user_id = get_current_user_id(token=token, db=db)
    if user_id != df_item.owner_id:
        raise HTTPException(status_code=403, detail="Forbidden: You do not have permission to access this DataFrame.") 
    df_json = df_item.df_json
    df = pd.read_json(df_json)
    
    pie_plot_fig = pie_plot(df) 
    encoded_fig = encode_fig(pie_plot_fig)
    
    return {"Pie plot": encoded_fig}