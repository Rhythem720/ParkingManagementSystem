from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import admin, bookings, feedback, slots, users
from ..import Base, engine
app = FastAPI()

Base.metadata.create_all(bind=engine)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(admin.router, prefix="/admin", tags=["admin"])
app.include_router(bookings.router, prefix="/bookings", tags=["bookings"])
app.include_router(feedback.router, prefix="/feedback", tags=["feedback"])
app.include_router(slots.router, prefix="/slots", tags=["slots"])
app.include_router(users.router, prefix="/users", tags=["users"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Parking Management System API"}