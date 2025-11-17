import ThreadList from "../../../components/forum/thread-list";
import { apiFetch } from "../../../lib/utils";
import { Category, Thread } from "../../../types/forum";
import { Button } from "../../../components/ui/button";

interface Params {
  params: { id: string };
}

export default async function CategoryDetail({ params }: Params) {
  const [category, threads] = await Promise.all([
    apiFetch<Category>(`/categories/${params.id}`),
    apiFetch<Thread[]>(`/threads?category_id=${params.id}`)
  ]);
  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-semibold">{category.name}</h1>
          <p className="text-slate-600">{category.description}</p>
        </div>
        <Button asChild>
          <a href={`/threads/new?category=${category.id}`}>New thread</a>
        </Button>
      </div>
      <ThreadList threads={threads} />
    </div>
  );
}
