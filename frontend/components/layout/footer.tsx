export default function Footer() {
  return (
    <footer className="bg-slate-100 dark:bg-slate-900 border-t">
      <div className="container mx-auto px-4 py-6 text-sm flex flex-col md:flex-row items-center justify-between gap-2">
        <span>© {new Date().getFullYear()} East Dulwich Forum</span>
        <div className="flex gap-4">
          <a href="/docs/code-of-conduct">Code of Conduct</a>
          <a href="/docs/privacy">Privacy</a>
        </div>
      </div>
    </footer>
  );
}
