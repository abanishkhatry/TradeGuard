

// This imports the main router component, which handles page navigation. It also imports the AuthProvider component that provides authentication context to the entire application.
import AppRouter from "./router";
import { AuthProvider } from "./context/AuthContext";

// The main App component wraps the AppRouter with the AuthProvider to ensure that all components within the app have access to authentication state and functions.
function App() {
  return (
    <AuthProvider>
      <AppRouter />
    </AuthProvider>
  );
}

export default App;
