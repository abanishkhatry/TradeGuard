"""
This file handles user authentication by verifying credentials and issuing JWT tokens for secure access.
"""

# API router from FastAPI to define routes related to authentication. Depends is used for dependency injection, allowing us to easily manage database sessions. HTTPException is used to raise HTTP errors when authentication fails.
from fastapi import APIRouter, Depends, HTTPException
# Importing Session from SQLAlchemy to interact with the database.
from sqlalchemy.orm import Session
# Importing the UserLogin schema to validate the login request data.
from app.schemas.user import UserLogin
# Importing the database session created in core/database.py. This is what creates the actual DB connection for each request.
from app.core.database import SessionLocal
# This is the SQLAlchemy model representing a row in the users table. We use this to query user data from the database.
from app.models.user import User
# this helps us to verify passwords.
from app.utils.password import verify_password
# This creates JWT tokens for authenticated users.
from app.core.security import create_access_token

# Creating an API router instance to define authentication-related routes.
router = APIRouter()

def get_db():
    # creates a new database session for each request and ensures it is closed after the request is completed.
    db = SessionLocal()
    try:
        yield db
    # This executes after the endpoint is done, ensuring the DB session is properly closed.
    finally:
        db.close()

# this declares an HTTP Post endpoint at the path /login, as the default router already has a prefix of /auth. So, this is actually accessible at /auth/login.
@router.post("/login")
# The login function takes a UserLogin object (which contains email and password) and a database session as parameters.
def login(user: UserLogin, db: Session = Depends(get_db)):
    # Query the database for a user with the provided email.
    db_user = db.query(User).filter(User.email == user.email).first()
    # If no user is found or the password does not match, raise an HTTP 401 Unauthorized error.
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    # If authentication is successful, create a JWT token for the user.
    token = create_access_token({"sub": db_user.email, "role": db_user.role})
    # Return the token in the response. 
    return {"access_token": token, "token_type": "bearer"}
