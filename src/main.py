from fastapi import FastAPI
import src.routers.plots_router as plots
import routers.upload_router as upload


app = FastAPI()

app.include_router(plots.router)
app.include_router(upload.router)



@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

    
