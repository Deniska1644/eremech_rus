from pydantic import BaseModel, EmailStr


class GetUser(BaseModel):
    username: str
    email: EmailStr

    class Config:
        orm_mode = True
        from_attributes = True


class RegUser(GetUser):
    password: str
