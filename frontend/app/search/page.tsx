"use client";

import { useState } from "react";
import { api } from "../../lib/api-client";
import { Button } from "../../components/ui/button";
import { Input } from "../../components/ui/input";
import { Card, CardContent } from "../../components/ui/card";

export default function SearchPage() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState<any[]>([]);

  async function handleSearch(e: React.FormEvent) {
    e.preventDefault();
    const { data } = await api.post("/search", { query });
    setResults(data.results);
  }

  return (
    <div className="space-y-4">
      <h1 className="text-3xl font-semibold">Search the forum</h1>
      <form className="flex gap-3" onSubmit={handleSearch}>
        <Input value={query} onChange={(e) => setQuery(e.target.value)} placeholder="Lost cat, plumber, babysitter..." />
        <Button type="submit">Search</Button>
      </form>
      <div className="space-y-3">
        {results.map((result) => (
          <Card key={result.id}>
            <CardContent>
              <p className="text-xs uppercase text-slate-400">{result.type}</p>
              <p className="font-semibold">{result.title}</p>
              <p className="text-sm text-slate-500">{result.excerpt}</p>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}
