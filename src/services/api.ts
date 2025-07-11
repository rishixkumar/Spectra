//------------------------------------------------------------------------
/**
 * API service layer for making HTTP requests to the backend using axios.
 *
 * - Sets the base URL from the REACT_APP_API_BASE_URL environment variable.
 * - Provides a utility to set or remove the Authorization header for JWT auth.
 */
import axios from "axios";
/**
 * Axios instance configured with the backend API base URL.
 */
const API = axios.create({
  baseURL: process.env.REACT_APP_API_BASE_URL,
});
//------------------------------------------------------------------------


/**
 * Sets or removes the Authorization header for all axios requests.
 * @param {string | null} token - JWT token to set, or null to remove the header.
 */
export const setAuthToken = (token: string | null) => {
  if (token) {
    API.defaults.headers.common["Authorization"] = `Bearer ${token}`;
  } else {
    delete API.defaults.headers.common["Authorization"];
  }
};
export default API;
//------------------------------------------------------------------------
