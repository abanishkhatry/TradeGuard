""" 
This file is responsible for creating JSON Web Tokens (JWTs) for user authentication.  JWTs are a compact and secure way to transmit information between parties as a JSON object. They are commonly used for authentication and authorization in web applications.
"""

# Importing the PyJWT library to create and manage JSON Web Tokens (JWTs).
import jwt
from datetime import datetime, timedelta
import os

# Load environment variables from a .env file into the application's environment.
SECRET_KEY = os.getenv("JWT_SECRET", "devsecret")
# The algorithm used to sign the JWTs. It is a symmetric algorithm that uses the same key for both signing and verification.
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# Function that creates a JWT access token. It takes a dictionary data as input, which typically contains user information (like user ID or email) that you want to include in the token's payload. Then it adds an expiration time to the token, encodes it using the SECRET_KEY and ALGORITHM, and returns the generated token.
def create_access_token(data: dict):
    # This line creates a copy of the input data dictionary to avoid modifying the original data.
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # This line adds an "exp" (expiration) claim to the token's payload, which indicates when the token should expire.
    to_encode.update({"exp": expire})
    # This line encodes the token using the specified SECRET_KEY and ALGORITHM, and returns the resulting JWT as a string.
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
