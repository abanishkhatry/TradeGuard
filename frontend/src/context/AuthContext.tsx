/* This file contains the AuthContext which manages authentication state (like storing the token) across the React application.*/ 

// createContext creates a global-like state object for authentication that can be accessed from any component in the app. useState is used to manage the token state, and useContext allows components to easily access the values from the context.
import React, { createContext, useState, useContext } from "react";

// Define the shape of the AuthContext
interface AuthContextType {
  // This stores the JWT token as a string or null if not logged in. 
  token: string | null;
  // Function to log in a user by setting the token. The token is then stored in state and localStorage.
  login: (token: string) => void;
  // Function to log out a user by clearing the token from state and localStorage.
  logout: () => void;
}

// Create the AuthContext with default null value.
const AuthContext = createContext<AuthContextType | null>(null);

// This is the component that will wrap your entire app. It provides the token state and login/logout functions to all child components.
export const AuthProvider = ({ children }: { children: React.ReactNode }) => {
    // Initialize the token state from localStorage if it exists. If the user has previously logged in, their token will be saved in localStorage. 
  const [token, setToken] = useState<string | null>(
    localStorage.getItem("token")
  );

  // Function to log in a user by setting the token in state and localStorage.
  const login = (token: string) => {
    setToken(token);
    localStorage.setItem("token", token);
  };

  // Function to log out a user by clearing the token from state and localStorage.
  const logout = () => {
    setToken(null);
    localStorage.removeItem("token");
  };

  // Provide the token, login, and logout functions to all child components.
  return (
    <AuthContext.Provider value={{ token, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

// Custom hook to easily access the AuthContext values in any component.
export const useAuth = () => {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth must be used inside AuthProvider");
  return ctx;
};
