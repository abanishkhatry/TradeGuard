"""
This file : defines the User model for the application using SQLAlchemy. The User model represents the users of the application and maps to the "users" table in the PostgreSQL database.
"""
# Column is used to define columns in the database table.
# Integer, String, and Boolean are data types for the columns. 
from sqlalchemy import Column, Integer, String, Boolean

# Importing the Base Class is essential because it registers the model with SQLAlchemy's ORM system and lets SQLAlchemy know that this class corresponds to a database table. If a function has inherited the Base class, SQLAlchemy knows that this class represents a table in the database. 
from app.core.database import Base

class User(Base):
    # Specifies the name of the table in the database that this model maps to.    
    __tablename__ = "users"

    # Here, id will a column name, and takes integer type as its value. primary_key = True indicates this column is the primary key for the table and SQLAlchemy will auto-create an incrementing integer value for each new user. index=True creates an index on this column, making lookups by id faster.
    id = Column(Integer, primary_key=True, index=True)
    
    # another column named email of type String. unique=True ensures that no two users can have the same email address in the database. index=True creates an index on this column for faster lookups. nullable=False means this column cannot be left empty.
    email = Column(String, unique=True, index=True, nullable=False)

    # column for storing the hashed password of the user. nullable=False means this column is required. We should never store plain text passwords for security reasons.
    hashed_password = Column(String, nullable=False)

    # column to specify the role of the user in the application. It defaults to "analyst". This can be used for role-based access control.
    role = Column(String, default="analyst") 

    # column to indicate whether the user's account is active. It defaults to True.
    is_active = Column(Boolean, default=True)
