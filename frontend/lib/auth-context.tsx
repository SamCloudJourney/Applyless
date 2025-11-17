"use client";

import { createContext, useContext, useEffect, useState } from "react";
import { api, setToken, clearToken } from "./api-client";

interface AuthState {
  user: any;
  login: (email: string, password: string) => Promise<void>;
  logout: () => void;
}

const AuthContext = createContext<AuthState | undefined>(undefined);

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<any>(null);

  useEffect(() => {
    async function bootstrap() {
      try {
        const stored = localStorage.getItem("edforum-token");
        if (stored) {
          setToken(stored);
          const { data } = await api.get("/users/");
          setUser(data?.find?.(() => true));
        }
      } catch {
        clearToken();
      }
    }
    bootstrap();
  }, []);

  async function login(email: string, password: string) {
    const { data } = await api.post("/auth/login", new URLSearchParams({ username: email, password }));
    setToken(data.access_token);
    setUser({ id: data.user_id, email: data.email, username: data.username });
  }

  function logout() {
    clearToken();
    setUser(null);
  }

  return <AuthContext.Provider value={{ user, login, logout }}>{children}</AuthContext.Provider>;
}

export function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) {
    throw new Error("useAuth must be used within AuthProvider");
  }
  return ctx;
}
