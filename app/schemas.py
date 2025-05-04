from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# User schema
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str
    role: str  # 'admin' or 'user'

class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

# Booking schema
class BookingCreate(BaseModel):
    user_id: int
    slot_id: int
    start_time: datetime
    end_time: datetime

class BookingBase(BookingCreate):
    pass

class Booking(BookingBase):
    id: int

    class Config:
        orm_mode = True

# Feedback schema
class FeedbackCreate(BaseModel):
    user_id: int
    message: str

class FeedbackBase(FeedbackCreate):
    pass

class Feedback(FeedbackBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

# Slot schema
class ParkingSlotCreate(BaseModel):
    id: int
    label: str
    status: str

class ParkingSlotUpdate(BaseModel):
    id:int
    status: str



        