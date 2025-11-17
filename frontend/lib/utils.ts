import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

import { serverApiBaseUrl } from "./config";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

export async function apiFetch<T>(path: string, options?: RequestInit): Promise<T> {
  const targetUrl = `${serverApiBaseUrl}${path}`;
  const response = await fetch(targetUrl, {
    cache: "no-store",
    ...options,
    headers: {
      "Content-Type": "application/json",
      ...(options?.headers || {})
    }
  });

  if (!response.ok) {
    let errorBody = "";
    try {
      errorBody = await response.text();
    } catch (error) {
      console.error("[apiFetch] Failed to read error body", error);
    }
    console.error("[apiFetch] Request failed", {
      url: targetUrl,
      status: response.status,
      statusText: response.statusText,
      body: errorBody?.slice(0, 512)
    });
    throw new Error(`API request failed with status ${response.status}`);
  }

  return response.json();
}
