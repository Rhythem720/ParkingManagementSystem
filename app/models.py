from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String)  # e.g., 'admin', 'user', etc.
    bookings = relationship("Booking", back_populates="user")

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    slot_id = Column(Integer, ForeignKey("parking_slots.id"))
    start_time = Column(String)  # Consider using a proper datetime type
    end_time = Column(String)  # Consider using a proper datetime type
    user = relationship("User", back_populates="bookings")
    parkingslot = relationship("ParkingSlot", back_populates="bookings")

class ParkingSlot(Base):
    __tablename__ = "parking_slots"

    id = Column(Integer, primary_key=True, index=True)
    label = Column(String, unique=True, index=True)
    status = Column(String, index=True)  
    bookings = relationship("Booking", back_populates="parkingslot")

class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    slot_id = Column(Integer, ForeignKey("parking_slots.id"))
    content = Column(String)
    rating = Column(Integer)  # e.g., 1 to 5 stars
    user = relationship("User", back_populates="feedback")
    parkingslot = relationship("ParkingSlot", back_populates="feedback")   