from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date

class ContactCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    birthday: date
    extra_info: Optional[str] = None

class ContactUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    birthday: Optional[date] = None
    extra_info: Optional[str] = None

class UserCreate(BaseModel):
    email: str
    password: str

class ContactInDB(ContactCreate):
    id: int

    class Config:
         from_attributes = True