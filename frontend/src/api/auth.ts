/** This file contains functions related to user authentication, such as logging in a user. After the user enters their email and password in the frontend, this file helps to connect it to the backend api and verify the information and return the user's token. */


// axios is used for making HTTP requests. It allows us to easily send requests to our backend API from the frontend by providing options like POST, GET, PUT, DELETE, requests. 
import axios from "axios";

// Base URL of the backend API. 
const API_URL = "http://localhost:8000";

// Function to log in a user by sending their email and password to the backend API.
export async function loginUser(email: string, password: string) {
  try {
    // Send a POST request to the /auth/login endpoint with email and password.
    const response = await axios.post(`${API_URL}/auth/login`, {
      email,
      password,
    });
    // Return the response data which contains the access token and token type.
    return response.data;
  } catch (error: any) {
    throw new Error(
      error?.response?.data?.detail || "Login failed. Please try again."
    );
  }
}

// Function to register a new user by sending their email and password to the backend API.
export async function registerUser(email: string, password: string) {
  try {
    // Send a POST request to the /auth/register endpoint with email and password.
    const response = await axios.post(`${API_URL}/auth/register`, {
      email,
      password,
    });

    // Return the response data from the backend (e.g. success message).
    return response.data;
  } catch (error: any) {
    // Extract a meaningful error message from the backend or fallback to a default message.
    throw new Error(
      error?.response?.data?.detail ||
        "Registration failed. Please try again."
    );
  }
}


