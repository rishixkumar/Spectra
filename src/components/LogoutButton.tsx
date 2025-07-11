//------------------------------------------------------------------------
/**
 * LogoutButton component for logging out the user.
 * Clears the authentication token and redirects to login page.
 */
import { useAuth } from "../store/AuthContext";
import { useNavigate } from "react-router-dom";

//------------------------------------------------------------------------
export default function LogoutButton() {
  const { setToken } = useAuth();
  const navigate = useNavigate();

//------------------------------------------------------------------------
  /**
   * Handles the logout action.
   */
  const handleLogout = () => {
    setToken(null);
    navigate("/login");
  };
  return <button onClick={handleLogout}>Logout</button>;
}
//------------------------------------------------------------------------ 