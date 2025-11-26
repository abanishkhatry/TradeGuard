// This files is the routing configuration for the React application. It defines the different routes (URLs) and the corresponding components that should be rendered when a user navigates to those routes.
import React from "react";
// imports necessary modules from react-router-dom for routing functionality. BrowserRouter is the router implementation for web applications that listens to changes in the browser URL and updates your UI dynamically without refreshing the page. Routes is a container for Route elements, and Route defines a mapping between a URL path and a component.
import { BrowserRouter, Routes, Route } from "react-router-dom";

// Import the Login page component to be used in the routing configuration.
import Login from "./pages/Login";
// Import the Register page component to be used in the routing configuration.
import Register from "./pages/Register";

// AppRouter component defines the routing structure of the application.
export default function AppRouter() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
      </Routes>
    </BrowserRouter>
  );
}
