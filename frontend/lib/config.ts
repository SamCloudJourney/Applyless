/**
 * Centralized configuration for API communication so both server-side fetch
 * helpers and client-side Axios calls share a normalized backend base URL.
 */
const API_SUFFIX = "/api/v1";
const ALLOWED_PROTOCOLS = new Set(["http:", "https:"]);
const LOCALHOST_PATTERNS = ["localhost", "127.0.0.1"];

const nodeEnv = process.env.NODE_ENV ?? "development";
const rawServerUrl = process.env.BACKEND_API_URL?.trim();
const rawPublicUrl = process.env.NEXT_PUBLIC_API_URL?.trim();
const developmentDefault = "http://localhost:8000/api/v1";

type NormalizedUrl = string;

function ensureProtocol(url: URL, label: string): void {
  if (!ALLOWED_PROTOCOLS.has(url.protocol)) {
    throw new TypeError(
      `${label} must use http or https (received protocol: ${url.protocol || ""})`
    );
  }
}

function ensureApiSuffix(base: string): NormalizedUrl {
  const trimmed = base.replace(/\/+$/, "");
  if (trimmed.endsWith(API_SUFFIX)) {
    return trimmed;
  }
  return `${trimmed}${API_SUFFIX}`;
}

function normalizeUrl(value: string, label: string): NormalizedUrl {
  try {
    const parsed = new URL(value);
    ensureProtocol(parsed, label);
    const pathname = parsed.pathname.replace(/\/+$/, "");
    const origin = parsed.origin;
    const base = pathname && pathname !== "/" ? `${origin}${pathname}` : origin;
    return ensureApiSuffix(base);
  } catch (error) {
    if (error instanceof TypeError) {
      throw error;
    }
    throw new Error(`${label} must be a valid absolute URL. Received: ${value}`);
  }
}

function ensureNotLocalhost(value: string, label: string): void {
  if (
    nodeEnv === "production" &&
    LOCALHOST_PATTERNS.some((pattern) => value.includes(pattern))
  ) {
    throw new Error(`${label} cannot point to localhost in production deployments.`);
  }
}

function resolveServerApiBaseUrl(): NormalizedUrl {
  if (rawServerUrl) {
    const normalized = normalizeUrl(rawServerUrl, "BACKEND_API_URL");
    ensureNotLocalhost(normalized, "BACKEND_API_URL");
    return normalized;
  }
  if (rawPublicUrl) {
    const normalized = normalizeUrl(
      rawPublicUrl,
      "NEXT_PUBLIC_API_URL (fallback for server-side fetches)"
    );
    ensureNotLocalhost(normalized, "NEXT_PUBLIC_API_URL");
    return normalized;
  }
  if (nodeEnv === "development") {
    return normalizeUrl(developmentDefault, "development default");
  }
  throw new Error(
    "BACKEND_API_URL is required for server-side rendering in production."
  );
}

function resolvePublicApiBaseUrl(): NormalizedUrl {
  if (rawPublicUrl) {
    const normalized = normalizeUrl(rawPublicUrl, "NEXT_PUBLIC_API_URL");
    ensureNotLocalhost(normalized, "NEXT_PUBLIC_API_URL");
    return normalized;
  }
  if (nodeEnv === "development") {
    return normalizeUrl(developmentDefault, "development default (public)");
  }
  throw new Error(
    "NEXT_PUBLIC_API_URL must be defined so the browser can reach the backend."
  );
}

export const serverApiBaseUrl = resolveServerApiBaseUrl();
export const publicApiBaseUrl = resolvePublicApiBaseUrl();

export const apiConfig = Object.freeze({
  nodeEnv,
  serverApiBaseUrl,
  publicApiBaseUrl
});
