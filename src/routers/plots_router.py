from fastapi import APIRouter, HTTPException, Depends, Cookie
from src.utils.utils import encode_fig
from src.utils.plots import time_plot, pie_plot
from src.utils.Data_holder import data_holder
from typing import Optional
import pandas as pd
from src.utils.session import verify_session_token


router = APIRouter(prefix="/plots")



@router.get("/time_plot/")
async def send_time_plot(df: Optional[pd.DataFrame] = Depends(data_holder.get_df),
                   file_name: Optional[str] = Depends(data_holder.get_name),
                   token: Optional[str] = Cookie(None)):
    
    verified = verify_session_token(file_name=file_name, token=token)
    if not verified:
        raise HTTPException(status_code=404, detail="upload a file first")
    
    if df is None:
        raise HTTPException(status_code=404, detail="DataFrame not found")
    
    time_plot_fig = time_plot(df) 
    encoded_fig = encode_fig(time_plot_fig)
    
    return {"Time plot": encoded_fig}



@router.get("/pie_plot/")
async def send_pie_plot(df: Optional[pd.DataFrame] = Depends(data_holder.get_df),
                  file_name: Optional[str] = Depends(data_holder.get_name),
                  token: Optional[str] = Cookie(None)):
    
    verified = verify_session_token(file_name=file_name, token=token)
    if not verified:
        raise HTTPException(status_code=404, detail="upload a file first")
     
    if df is None:
        raise HTTPException(status_code=404, detail="upload a file first")
    
    pie_plot_fig = pie_plot(df) 
    encoded_fig = encode_fig(pie_plot_fig)
    
    return {"Pie plot": encoded_fig}