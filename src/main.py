from fastapi import FastAPI
from src.routers import plots, upload, auth 
from src.db.database import engine
from src.db.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(plots.router)
app.include_router(upload.router)
app.include_router(auth.router)


    
