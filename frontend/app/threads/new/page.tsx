"use client";

import { useEffect, useState } from "react";
import { useSearchParams, useRouter } from "next/navigation";
import { api } from "../../../lib/api-client";
import { Button } from "../../../components/ui/button";
import { Input } from "../../../components/ui/input";
import { Textarea } from "../../../components/ui/textarea";
import { Category } from "../../../types/forum";

export default function NewThreadPage() {
  const params = useSearchParams();
  const router = useRouter();
  const [categories, setCategories] = useState<Category[]>([]);
  const [categoryId, setCategoryId] = useState<string>(params.get("category") || "");
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");

  useEffect(() => {
    async function load() {
      const { data } = await api.get<Category[]>("/categories");
      setCategories(data);
    }
    load();
  }, []);

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    const { data } = await api.post("/threads", { category_id: categoryId, title });
    await api.post("/posts", { thread_id: data.id, content });
    router.push(`/threads/${data.id}`);
  }

  return (
    <div className="max-w-2xl space-y-4">
      <h1 className="text-3xl font-semibold">Start a new discussion</h1>
      <form className="space-y-3" onSubmit={handleSubmit}>
        <label className="text-sm font-medium">Category</label>
        <select
          className="w-full rounded-md border border-slate-200 p-2"
          value={categoryId}
          onChange={(e) => setCategoryId(e.target.value)}
          required
        >
          <option value="">Select a category</option>
          {categories.map((category) => (
            <option key={category.id} value={category.id}>
              {category.name}
            </option>
          ))}
        </select>
        <Input value={title} onChange={(e) => setTitle(e.target.value)} placeholder="Thread title" required />
        <Textarea value={content} onChange={(e) => setContent(e.target.value)} placeholder="Kick off the discussion..." />
        <Button type="submit">Publish thread</Button>
      </form>
    </div>
  );
}
