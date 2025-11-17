import ThreadList from "../../components/forum/thread-list";
import { apiFetch } from "../../lib/utils";
import { Thread } from "../../types/forum";

export default async function ThreadsPage() {
  const threads = await apiFetch<Thread[]>("/threads");
  return (
    <div className="space-y-4">
      <h1 className="text-3xl font-semibold">All threads</h1>
      <ThreadList threads={threads} />
    </div>
  );
}
