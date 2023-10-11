from fastapi import FastAPI
from fastapi.responses import JSONResponse 

app = FastAPI()

@app.get("/")
async def root():
    res:dict = {
        "status": "Running..."
    }
    return JSONResponse(content=res, status_code=200)