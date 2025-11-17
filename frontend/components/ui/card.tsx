import { cn } from "../../lib/utils";

export function Card({ children, className }: { children: React.ReactNode; className?: string }) {
  return <div className={cn("rounded-xl border border-slate-200 bg-white shadow-sm dark:bg-slate-900", className)}>{children}</div>;
}

export function CardHeader({ children }: { children: React.ReactNode }) {
  return <div className="border-b border-slate-100 px-6 py-4">{children}</div>;
}

export function CardContent({ children }: { children: React.ReactNode }) {
  return <div className="px-6 py-4 space-y-3">{children}</div>;
}
