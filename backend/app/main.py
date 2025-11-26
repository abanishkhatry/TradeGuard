# imports FastAPI framework class which helps to create the main API application instance, register routers for different endpoints, and manage the overall application configuration.
from fastapi import FastAPI
# Importing the auth and users modules which contain the API routes for authentication and new user management respectively.
from app.api import auth, users
# Importing Base and engine from database module to create the database tables based on the defined SQLAlchemy models.
from app.core.database import Base, engine

# Importing CORSMiddleware to handle Cross-Origin Resource Sharing (CORS) which allows or restricts resources on a web server to be requested from another domain outside the domain from which the resource originated.
from fastapi.middleware.cors import CORSMiddleware

# List of allowed origins for CORS. Here, we are allowing requests from the frontend development server running on localhost at port 5173.
origins = [
    "http://localhost:5173", # frontend dev server
    "http://127.0.0.1:5173"
]
# This line creates all the database tables defined in the SQLAlchemy models if they do not already exist.
Base.metadata.create_all(bind=engine)

# Creating the main FastAPI application instance.
app = FastAPI()
# Adding CORS middleware to the FastAPI application to handle cross-origin requests from the specified origins.
app.add_middleware(
    CORSMiddleware,
    # Specifies which origins are allowed to make cross-origin requests to the API.
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# This attaches the authentication routes to the main API application under the /auth prefix.
app.include_router(auth.router, prefix="/auth", tags=["auth"])
# This attaches the user management routes to the main API application under the /admin prefix.
app.include_router(users.router, prefix="/admin", tags=["users"])
