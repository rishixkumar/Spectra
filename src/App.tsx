//------------------------------------------------------------------------
/**
 * App component sets up routing and authentication context for the application.
 * Includes public and protected routes.
 */
import React, { type JSX } from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import { AuthProvider, useAuth } from "./store/AuthContext";
import Signup from "./pages/Signup";
import Login from "./pages/Login";
// import Dashboard, Watchlist, etc. as you build them
//------------------------------------------------------------------------
/**
 * PrivateRoute component to protect routes that require authentication.
 * @param {object} props
 * @param {JSX.Element} props.children - The protected component
 * @returns {JSX.Element}
 */
function PrivateRoute({ children }: { children: JSX.Element }) {
  const { token } = useAuth();
  return token ? children : <Navigate to="/login" />;
}
//------------------------------------------------------------------------
export default function App() {
  return (
    <AuthProvider>
      <Router>
        <Routes>
          <Route path="/signup" element={<Signup />} />
          <Route path="/login" element={<Login />} />
          {/* Example protected route: */}
          {/* <Route path="/dashboard" element={<PrivateRoute><Dashboard /></PrivateRoute>} /> */}
          <Route path="*" element={<Navigate to="/login" />} />
        </Routes>
      </Router>
    </AuthProvider>
  );
}
//------------------------------------------------------------------------
