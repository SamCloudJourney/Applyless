"use client";

import { useEffect, useState } from "react";
import { api } from "../../lib/api-client";
import { Card, CardContent, CardHeader } from "../../components/ui/card";

export default function AdminPage() {
  const [stats, setStats] = useState<Record<string, number>>({});

  useEffect(() => {
    async function load() {
      const { data } = await api.get<Record<string, number>>("/admin/stats");
      setStats(data);
    }
    load();
  }, []);

  return (
    <div className="space-y-4">
      <h1 className="text-3xl font-semibold">Admin dashboard</h1>
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        {Object.entries(stats).map(([key, value]) => (
          <Card key={key}>
            <CardHeader className="text-sm uppercase text-slate-500">{key.replace("_", " ")}</CardHeader>
            <CardContent>
              <p className="text-3xl font-semibold">{value}</p>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}
