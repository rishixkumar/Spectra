//------------------------------------------------------------------------
/**
 * Signup page for user registration.
 * Allows users to create a new account by providing email and password.
 */
import React, { useState } from "react";
import API from "../services/api";
import { useNavigate } from "react-router-dom";
//------------------------------------------------------------------------
export default function Signup() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const navigate = useNavigate();
//------------------------------------------------------------------------
  /**
   * Handles the signup form submission.
   * @param {React.FormEvent} e - Form event
   */
  const handleSignup = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    try {
      await API.post("/users/register", { email, password });
      navigate("/login");
    } catch (err: any) {
      setError(err.response?.data?.detail || "Signup failed");
    }
  };
//------------------------------------------------------------------------
  return (
    <>
      <form onSubmit={handleSignup}>
        <h2>Sign Up</h2>
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
        <button type="submit">Sign Up</button>
        {error && <div style={{ color: "red" }}>{error}</div>}
      </form>
      {/* ------------------------------------------------------------------------ */}
      <div style={{ marginTop: 16 }}>
        <span>Already have an account? </span>
        <button type="button" style={{ color: 'blue', background: 'none', border: 'none', textDecoration: 'underline', cursor: 'pointer' }} onClick={() => navigate('/login')}>
          Login
        </button>
      </div>
    </>
  );
}
//------------------------------------------------------------------------ 