from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: str | None = None

class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True  # Replace orm_mode with from_attributes
