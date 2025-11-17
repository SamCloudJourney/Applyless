import axios from "axios";

import { publicApiBaseUrl } from "./config";

export const api = axios.create({
  baseURL: publicApiBaseUrl,
  headers: {
    "Content-Type": "application/json"
  }
});

api.interceptors.request.use((config) => {
  if (typeof window !== "undefined") {
    const token = localStorage.getItem("edforum-token");
    if (token) {
      config.headers = config.headers ?? {};
      config.headers.Authorization = `Bearer ${token}`;
    }
  }
  return config;
});

export function setToken(token: string) {
  if (typeof window !== "undefined") {
    localStorage.setItem("edforum-token", token);
  }
}

export function clearToken() {
  if (typeof window !== "undefined") {
    localStorage.removeItem("edforum-token");
  }
}
