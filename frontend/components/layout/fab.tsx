"use client";

import Link from "next/link";
import { Pencil } from "lucide-react";

export default function FloatingComposer() {
  return (
    <Link
      href="/threads/new"
      className="fixed bottom-6 right-6 bg-brand text-white rounded-full shadow-2xl px-5 py-3 flex items-center gap-2"
    >
      <Pencil className="h-4 w-4" /> New thread
    </Link>
  );
}
