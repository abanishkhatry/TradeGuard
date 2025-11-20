
# Pydantic is commonly used in FastAPI for data validation and serialization.
# BaseModel is the base class for creating Pydantic models. Every schema will inherit from this class as it provides validation, type checking, data serialization, and data parsing. 
# EmailStr is a specialized type provided by Pydantic to validate email addresses.
from pydantic import BaseModel, EmailStr

# Schema for creating a new user. It includes email, password, and an optional role (defaulting to "analyst").
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role: str = "analyst"

# Schema for user login which includes email and password.
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Schema for outputting user information. It includes id, email, and role. This is after the user is created or fetched from the database.
class UserOut(BaseModel):
    id: int
    email: EmailStr
    role: str
    # Enables compatibility with ORM objects, allowing automatic conversion from SQLAlchemy models to Pydantic models. This is because Pydantic expects dictionary-like objects by default but SQLAlchemy returns ORM objects. So, this setting allows Pydantic to read data directly from ORM models.
    class Config:
        orm_mode = True
