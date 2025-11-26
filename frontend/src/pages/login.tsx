
// This file contains the Login page component which provides a user interface for users to log in to the TradeGuard application. It includes form fields for email and password, handles form submission, and manages error states.

import React from "react";
// React and useState are imported to create the functional component and manage local state for form inputs and error messages.
import { useState } from "react";
// Import the loginUser function from the auth API to handle user login requests and the useAuth hook from AuthContext to manage authentication state.
import { loginUser } from "../api/auth";
import { useAuth } from "../context/AuthContext";
// Import Button and Input components from the UI library for consistent styling and functionality.
import { Button } from "../components/ui/button";
import { Input } from "../components/ui/input";


export default function Login() {
  // calls the useAuth hook to get the login function from AuthContext. 
  const { login } = useAuth();
  // Local state to manage email, password, and error messages.
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  // Function to handle form submission when the user attempts to log in.
  async function handleSubmit(e: React.FormEvent) {
    // Prevent the default form submission behavior, by stopping the page from reloading.
    e.preventDefault();
    setError("");
    // 
    try {
      // This sends the email and password to the backend API using the loginUser function. Then it waits for the backend's response , if valid, it retrieves the access token from the response data. 
      const data = await loginUser(email, password);
      // Calls the login function from AuthContext to store the token in state and localStorage.
      login(data.access_token);
        // Redirects the user to the dashboard page after successful login.
      window.location.href = "/dashboard";
    } 
    // If there's an error during login (like invalid credentials), it catches the error and sets the error message to be displayed to the user.
    catch (err: any) {
      setError(err.message);
    }
  }

  // component returns the login page UI. It includes a form with input fields for email and password, and a submit button. If there's an error message, it displays it above the form.
  return (
    <div className="h-screen flex items-center justify-center">
      <form
        onSubmit={handleSubmit}
        className="p-6 w-[350px] border rounded-xl shadow-lg flex flex-col gap-3"
      >
        <h1 className="text-xl font-bold text-center">TradeGuard Login</h1>

        {error && (
          <p className="text-red-600 text-sm text-center">{error}</p>
        )}

        <Input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />

        <Input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <Button type="submit" className="w-full">
          Login
        </Button>
      </form>
    </div>
  );
}
