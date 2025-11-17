"use client";

import ReactMarkdown from "react-markdown";
import { Post } from "../../types/forum";
import { Card, CardContent, CardHeader } from "../ui/card";

export default function PostList({ posts }: { posts: Post[] }) {
  return (
    <div className="space-y-4">
      {posts.map((post) => (
        <Card key={post.id}>
          <CardHeader>
            <div className="flex items-center justify-between text-sm text-slate-500">
              <span>{post.author?.username ?? "Anonymous"}</span>
              <span>{new Date(post.created_at).toLocaleString()}</span>
            </div>
          </CardHeader>
          <CardContent>
            <ReactMarkdown className="prose dark:prose-invert max-w-none">{post.content}</ReactMarkdown>
          </CardContent>
        </Card>
      ))}
    </div>
  );
}
