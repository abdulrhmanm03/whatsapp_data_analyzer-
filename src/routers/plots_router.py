from fastapi import APIRouter, HTTPException, Depends
from src.utils.utils import time_plot, pie_plot, encode_fig
from ..utils.Data_holder import data_holder
from typing import Optional
import pandas as pd


router = APIRouter(prefix="/plots")

@router.get("/time_plot/")
async def send_time_plot(df: Optional[pd.DataFrame] = Depends(lambda: data_holder.df)):
    
    if df is None:
        raise HTTPException(status_code=404, detail="DataFrame not found")
    
    time_plot_fig = time_plot(df) 
    encoded_fig = encode_fig(time_plot_fig)
    
    return {"Time plot": encoded_fig}

@router.get("/pie_plot/")
async def send_pie_plot(df: Optional[pd.DataFrame] = Depends(lambda: data_holder.df)):
    
    if df is None:
        raise HTTPException(status_code=404, detail="DataFrame not found")
    
    pie_plot_fig = pie_plot(df) 
    encoded_fig = encode_fig(pie_plot_fig)
    
    return {"Pie plot": encoded_fig}