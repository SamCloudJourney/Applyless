"use client";

import dynamic from "next/dynamic";
import { useState } from "react";
import { Button } from "../ui/button";
import { api } from "../../lib/api-client";

const MDEditor = dynamic(() => import("@uiw/react-md-editor"), { ssr: false });

interface Props {
  threadId: string;
  onPosted?: () => void;
}

export default function PostEditor({ threadId, onPosted }: Props) {
  const [content, setContent] = useState<string>("### What's happening in SE22?");
  const [loading, setLoading] = useState(false);

  async function handleSubmit() {
    setLoading(true);
    try {
      await api.post("/posts", { thread_id: threadId, content });
      setContent("");
      onPosted?.();
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="rounded-xl border bg-white shadow-sm dark:bg-slate-900 p-4 space-y-3" data-color-mode="light">
      <MDEditor value={content} onChange={(value) => setContent(value || "")} height={200} />
      <div className="flex justify-end">
        <Button disabled={loading} onClick={handleSubmit}>
          {loading ? "Posting..." : "Post reply"}
        </Button>
      </div>
    </div>
  );
}
