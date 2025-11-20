""" 
Passlib is a password hashing library for Python. It provides a simple and secure way to hash and verify passwords using various hashing algorithms.

CryptContext is a helper class that manages which hashing algorithms you want to use, how to configure them, how to upgrade hashes over time, and more. Its basically a password security manager that stores your hashing rules. 

"""

from passlib.context import CryptContext

# creates a password hashing context, where we specify that we want to use the bcrypt hashing algorithm. The deprecated="auto" argument means that if we ever change our hashing scheme in the future, Passlib will automatically recognize and handle old hashes created with previous algorithms.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# function whose job is to convert the plain text passwords into secure hashed passwords. 
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# function that checks whether a given plain text password matches a previously hashed password in the database.
def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)
