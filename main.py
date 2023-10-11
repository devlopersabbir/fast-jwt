from fastapi import FastAPI
from fastapi.responses import JSONResponse
from routes.users.userRoutes import router as userRoutes

app = FastAPI()
app.include_router(userRoutes)

@app.get("/")
async def root():
    res:dict = {
        "status": "Running..."
    }
    return JSONResponse(content=res, status_code=200)