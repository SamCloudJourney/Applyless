import PostList from "../../../components/forum/post-list";
import PostEditor from "../../../components/forum/post-editor";
import { apiFetch } from "../../../lib/utils";
import { Post, Thread } from "../../../types/forum";
import { Button } from "../../../components/ui/button";

interface Params {
  params: { id: string };
}

async function getData(threadId: string) {
  const [thread, posts] = await Promise.all([
    apiFetch<Thread>(`/threads/${threadId}`),
    apiFetch<Post[]>(`/posts/thread/${threadId}`)
  ]);
  return { thread, posts };
}

export default async function ThreadPage({ params }: Params) {
  const { thread, posts } = await getData(params.id);
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <p className="text-sm uppercase tracking-wider text-slate-400">Thread</p>
          <h1 className="text-3xl font-semibold">{thread.title}</h1>
        </div>
        <Button asChild variant="outline">
          <a href="#reply">Reply</a>
        </Button>
      </div>
      <PostList posts={posts} />
      <div id="reply">
        <PostEditor threadId={thread.id} />
      </div>
    </div>
  );
}
