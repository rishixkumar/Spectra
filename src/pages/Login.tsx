//------------------------------------------------------------------------
/**
 * Login page for user authentication.
 * Allows users to log in with email and password and stores the JWT token.
 */
import React, { useState } from "react";
import API from "../services/api";
import { useAuth } from "../store/AuthContext";
import { useNavigate } from "react-router-dom";
//------------------------------------------------------------------------
export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const { setToken } = useAuth();
  const navigate = useNavigate();
//------------------------------------------------------------------------
  /**
   * Handles the login form submission.
   * @param {React.FormEvent} e - Form event
   */
  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    try {
      const params = new URLSearchParams();
      params.append("username", email);
      params.append("password", password);
      const res = await API.post("/users/login", params, {
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
      });
      const data = res.data as { access_token: string };
      setToken(data.access_token);
      navigate("/dashboard");
    } catch (err: any) {
      setError(err.response?.data?.detail || "Login failed");
    }
  };
//------------------------------------------------------------------------
  return (
    <>
      <form onSubmit={handleLogin}>
        <h2>Login</h2>
        <input
          type="email"
          value={email}
          onChange={e => setEmail(e.target.value)}
          placeholder="Email"
          required
        />
        <input
          type="password"
          value={password}
          onChange={e => setPassword(e.target.value)}
          placeholder="Password"
          required
        />
        <button type="submit">Login</button>
        {error && <div style={{ color: "red" }}>{error}</div>}
      </form>
      {/* ------------------------------------------------------------------------ */}
      <div style={{ marginTop: 16 }}>
        <span>Don't have an account? </span>
        <button type="button" style={{ color: 'blue', background: 'none', border: 'none', textDecoration: 'underline', cursor: 'pointer' }} onClick={() => navigate('/signup')}>
          Sign Up
        </button>
      </div>
    </>
  );
}
//------------------------------------------------------------------------ 