from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from schemas.users.userSchema import CreateUserReqest
from controllers.userControllers import createUserController

router = APIRouter(
    prefix="/users",
    tags=["User"],
    responses={
        404,
        {
            "message": "Not Found!"
        }
    }
)

@router.post("", status_code=status.HTTP_201_CREATED)
async def createUser(data: CreateUserReqest, db: Session = Depends(get_db)):
    try:
        await createUserController(data=data, db=db)
    except Exception as error:
        print("____________ ERRO ____________", error)