import type { Metadata } from "next";
import "./globals.css";
import { Inter } from "next/font/google";
import Providers from "../components/layout/providers";
import Header from "../components/layout/header";
import Footer from "../components/layout/footer";
import FloatingComposer from "../components/layout/fab";

const inter = Inter({ subsets: ["latin"], variable: "--font-inter" });

export const metadata: Metadata = {
  title: "East Dulwich Forum",
  description: "Hyper-local conversations for SE22",
  metadataBase: new URL("https://east-dulwich.local")
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className="antialiased">
      <body className={`${inter.variable} font-sans`}>
        <Providers>
          <div className="min-h-screen flex flex-col">
            <Header />
            <main className="flex-1 container mx-auto px-4 py-6">{children}</main>
            <Footer />
          </div>
          <FloatingComposer />
        </Providers>
      </body>
    </html>
  );
}
