import axios from 'axios';

const API = axios.create({
  baseURL: process.env.REACT_APP_API_BASE_URL || 'http://localhost:5000/api'
});

export const registerUser = (data) => API.post('/auth/register', data);
export const loginUser = (data) => API.post('/auth/login', data);
export const detectThreat = (data, token) =>
  API.post('/threats/detect', data, {
    headers: { Authorization: `Bearer ${token}` }
  });
