import type { Config } from "tailwindcss";
import { fontFamily } from "tailwindcss/defaultTheme";

const config: Config = {
  darkMode: ["class"],
  content: ["./app/**/*.{ts,tsx}", "./components/**/*.{ts,tsx}"],
  theme: {
    extend: {
      fontFamily: {
        sans: ["Inter", ...fontFamily.sans]
      },
      colors: {
        brand: {
          DEFAULT: "#1B998B",
          dark: "#157A70",
          light: "#67D5C0"
        }
      }
    }
  },
  plugins: [require("tailwindcss-animate"), require("@tailwindcss/typography")]
};

export default config;
