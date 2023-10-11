from models.userModel import UserModel
from security.service import hashPassword
from fastapi.exceptions import HTTPException
from fastapi import status
from fastapi.responses import JSONResponse
from datetime import datetime

async def createUserController(data, db):
    user = db.query(UserModel).filter(UserModel.email == data.email).first()

    if user:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Email is already exis!")
    
    newUser = UserModel(
        email= data.email,
        password = hashPassword(data.password),
        created_at = datetime.now()
    )

    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "message": "User created successfully!",
            "user": newUser
        }
    )