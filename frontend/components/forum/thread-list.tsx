"use client";

import Link from "next/link";
import { Thread } from "../../types/forum";
import { Card, CardContent, CardHeader } from "../ui/card";

export default function ThreadList({ threads }: { threads: Thread[] }) {
  if (!threads.length) {
    return <p className="text-sm text-slate-500">No threads yet. Be the first to post!</p>;
  }
  return (
    <div className="space-y-3">
      {threads.map((thread) => (
        <Card key={thread.id}>
          <CardHeader>
            <div className="flex items-center justify-between">
              <Link href={`/threads/${thread.id}`} className="font-semibold hover:text-brand">
                {thread.title}
              </Link>
              <span className="text-xs text-slate-500">Trusted score {thread.trusted_score ?? 0}</span>
            </div>
          </CardHeader>
          <CardContent>
            <p className="text-sm text-slate-500">Started by {thread.author?.username ?? "Anonymous"}</p>
          </CardContent>
        </Card>
      ))}
    </div>
  );
}
