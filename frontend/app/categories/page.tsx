import Link from "next/link";
import { apiFetch } from "../../lib/utils";
import { Category } from "../../types/forum";
import { Card, CardContent, CardHeader } from "../../components/ui/card";

export default async function CategoriesPage() {
  const categories = await apiFetch<Category[]>("/categories");
  return (
    <div className="space-y-4">
      <h1 className="text-3xl font-semibold">Explore categories</h1>
      <div className="grid gap-4 md:grid-cols-2">
        {categories.map((category) => (
          <Card key={category.id}>
            <CardHeader>
              <Link href={`/categories/${category.id}`} className="text-xl font-semibold">
                {category.name}
              </Link>
            </CardHeader>
            <CardContent>
              <p className="text-slate-600">{category.description}</p>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}
