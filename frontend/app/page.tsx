import Link from "next/link";
import ThreadList from "../components/forum/thread-list";
import LocalMap from "../components/forum/local-map";
import { apiFetch } from "../lib/utils";
import { Thread, Category } from "../types/forum";
import { Card, CardContent, CardHeader } from "../components/ui/card";

async function getHomeData() {
  const [categories, threads] = await Promise.all([
    apiFetch<Category[]>("/categories"),
    apiFetch<Thread[]>("/threads?limit=5")
  ]);
  return { categories, threads };
}

export default async function HomePage() {
  const { categories, threads } = await getHomeData();
  return (
    <div className="space-y-8">
      <section className="grid gap-4 lg:grid-cols-3">
        <Card className="lg:col-span-2 bg-gradient-to-r from-brand to-brand-light text-white">
          <CardHeader>
            <h1 className="text-3xl font-semibold">Welcome back to SE22</h1>
          </CardHeader>
          <CardContent>
            <p className="text-lg">
              Discover trusted recommendations, local events, lost &amp; found posts, and more from the East Dulwich community.
            </p>
            <div className="mt-4 flex flex-wrap gap-3">
              <Link href="/threads/new" className="px-4 py-2 rounded-full bg-white text-brand font-medium">
                Start a thread
              </Link>
              <Link href="/search" className="px-4 py-2 rounded-full border border-white text-white">
                Search discussions
              </Link>
            </div>
          </CardContent>
        </Card>
        <LocalMap />
      </section>

      <section>
        <div className="flex items-center justify-between mb-4">
          <h2 className="text-2xl font-semibold">Hot categories</h2>
          <Link href="/categories" className="text-brand">
            View all
          </Link>
        </div>
        <div className="grid gap-4 md:grid-cols-3">
          {categories.slice(0, 6).map((category) => (
            <Card key={category.id}>
              <CardHeader>
                <Link href={`/categories/${category.id}`} className="font-semibold">
                  {category.name}
                </Link>
              </CardHeader>
              <CardContent>
                <p className="text-sm text-slate-500">{category.description}</p>
              </CardContent>
            </Card>
          ))}
        </div>
      </section>

      <section>
        <div className="flex items-center justify-between mb-4">
          <h2 className="text-2xl font-semibold">Latest threads</h2>
          <Link href="/threads" className="text-brand">
            Browse threads
          </Link>
        </div>
        <ThreadList threads={threads} />
      </section>
    </div>
  );
}
