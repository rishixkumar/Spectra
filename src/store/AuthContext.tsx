//------------------------------------------------------------------------
/**
 * AuthContext provides authentication state and token management for the app.
 *
 * @typedef {Object} AuthContextType
 * @property {string | null} token - The JWT token or null if not authenticated.
 * @property {(token: string | null) => void} setToken - Function to set the token.
 */
import React, { createContext, useContext, useState } from "react";
import { setAuthToken } from "../services/api";

interface AuthContextType {
  token: string | null;
  setToken: (token: string | null) => void;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

/**
 * AuthProvider wraps the app and provides authentication context.
 * @param {object} props
 * @param {React.ReactNode} props.children - Child components
 */
export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [token, setTokenState] = useState<string | null>(() => localStorage.getItem("token"));

  const setToken = (token: string | null) => {
    setTokenState(token);
    if (token) {
      localStorage.setItem("token", token);
    } else {
      localStorage.removeItem("token");
    }
    setAuthToken(token);
  };

  // Ensure axios always has the latest token
  React.useEffect(() => {
    setAuthToken(token);
  }, [token]);

  return (
    <AuthContext.Provider value={{ token, setToken }}>
      {children}
    </AuthContext.Provider>
  );
};

//------------------------------------------------------------------------
/**
 * useAuth hook to access authentication context.
 * @returns {AuthContextType}
 * @throws {Error} If used outside AuthProvider
 */
export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) throw new Error("useAuth must be used within AuthProvider");
  return context;
};
//------------------------------------------------------------------------ 