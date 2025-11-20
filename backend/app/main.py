# imports FastAPI framework class which helps to create the main API application instance, register routers for different endpoints, and manage the overall application configuration.
from fastapi import FastAPI
# Importing the auth and users modules which contain the API routes for authentication and new user management respectively.
from app.api import auth, users
# Importing Base and engine from database module to create the database tables based on the defined SQLAlchemy models.
from app.core.database import Base, engine

# This line creates all the database tables defined in the SQLAlchemy models if they do not already exist.
Base.metadata.create_all(bind=engine)

# Creating the main FastAPI application instance.
app = FastAPI()
# This attaches the authentication routes to the main API application under the /auth prefix.
app.include_router(auth.router, prefix="/auth", tags=["auth"])
# This attaches the user management routes to the main API application under the /admin prefix.
app.include_router(users.router, prefix="/admin", tags=["users"])
