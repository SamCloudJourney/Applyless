"use client";

import Link from "next/link";
import { useTheme } from "next-themes";
import { useState } from "react";
import { Menu, Sun, Moon } from "lucide-react";

export default function Header() {
  const { theme, setTheme } = useTheme();
  const [open, setOpen] = useState(false);
  const navItems = [
    { href: "/", label: "Home" },
    { href: "/categories", label: "Categories" },
    { href: "/search", label: "Search" },
    { href: "/notifications", label: "Notifications" },
    { href: "/admin", label: "Admin" }
  ];
  return (
    <header className="bg-white/70 dark:bg-slate-900/60 backdrop-blur border-b sticky top-0 z-30">
      <div className="container mx-auto px-4 py-3 flex items-center justify-between">
        <Link href="/" className="font-semibold text-lg">
          East Dulwich Forum
        </Link>
        <nav className="hidden md:flex items-center gap-4">
          {navItems.map((item) => (
            <Link key={item.href} href={item.href} className="hover:text-brand">
              {item.label}
            </Link>
          ))}
          <button
            className="p-2 rounded-full bg-slate-100 dark:bg-slate-800"
            onClick={() => setTheme(theme === "dark" ? "light" : "dark")}
          >
            {theme === "dark" ? <Sun className="w-4 h-4" /> : <Moon className="w-4 h-4" />}
          </button>
        </nav>
        <button className="md:hidden" onClick={() => setOpen(!open)}>
          <Menu />
        </button>
      </div>
      {open && (
        <div className="md:hidden px-4 pb-4 space-y-2">
          {navItems.map((item) => (
            <Link key={item.href} href={item.href} className="block" onClick={() => setOpen(false)}>
              {item.label}
            </Link>
          ))}
        </div>
      )}
    </header>
  );
}
