""" 
This file : helps to connect the FastAPI app to the PostgreSQL database using SQLAlchemy.

SQLAlchemy : is used as the ORM (Object Relational Mapper) to allow us to work with a database using Python classes and objects instead of manually writing SQL queries. 

"""

# create_engine creates a database connection object that SQLAlchemy uses to interact with the database.
from sqlalchemy import create_engine

# sessionmaker creates database sessions for performing operations on the database. A session is a single conversation with the database where operations like queries, inserts, updates, and deletes are executed.
# declarative_base is a factory function that constructs a base class for all the database models we will define later. SQLAlchemy uses this base class to map Python classes to database tables.
from sqlalchemy.orm import sessionmaker, declarative_base

from app.core.config import settings


# creates the database engine using the connection string. The engine will handle the actual connection to the database.
engine = create_engine(settings.DATABASE_URL, echo = False)
# creates a configured "Session" class that will be used to create session objects for interacting with the database.
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# creates a base class for our database models to inherit from.
Base = declarative_base()
