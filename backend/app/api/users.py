""" 
This file helps to manage user-related API endpoints. Here, it helps to add new user to the database and returns the created user details.
"""

# APIRouter helps to create modular route handlers and Depends is used for automatically inject a database session into the route. 
from fastapi import APIRouter, Depends
# SQLAlchemy's Session is used to interact with the database.
from sqlalchemy.orm import Session
# Getting the necessary schemas , UserCreate for incoming user data and UserOut for outgoing user data.
from app.schemas.user import UserCreate, UserOut
# Importing the User model to interact with the users table in the database.
from app.models.user import User
# Importing a utility function to hash passwords before storing them in the database.
from app.utils.password import hash_password
# SessionLocal is a factory that creates database sessions.
from app.core.database import SessionLocal

# Creating an APIRouter instance to define user-related routes. 
router = APIRouter()

# Function to get a database session. 
def get_db():
    # creates an active connection to the database
    db = SessionLocal()
    try:
        # this gives the session to the route function that needs it. 
        yield db
    # once the route is done using the session, it will be closed to free up resources.
    finally:
        db.close()

# this route/logic handles POST requests to create a new user.
# This also tells FastAPI to convert the SQLAlchemy model into a UserOut Schema before returning it as a response.
@router.post("/users", response_model=UserOut)
# The create_user function takes in user data and a database session.
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Creating a new User instance with the provided email, hashed password, and role.
    new_user = User(
        email=user.email,
        hashed_password=hash_password(user.password),
        role=user.role
    )
    # Adding the new user to the database session, committing the transaction, and refreshing the instance to get the latest data from the database.
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    # Returning the newly created user.
    return new_user
