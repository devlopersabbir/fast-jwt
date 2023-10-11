from pydantic import BaseModel, EmailStr

class CreateUserReqest(BaseModel):
    name: str
    email: EmailStr
    password: str