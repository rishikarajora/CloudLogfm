import axios from "axios";

const API = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
});

export const analyzeIncident = async (payload) => {
  const response = await API.post(
    "/analyze",
    payload
  );

  return response.data;
};