import { apiFetch } from "../../../lib/utils";
import { User } from "../../../types/forum";
import { Card, CardContent } from "../../../components/ui/card";

interface Params {
  params: { username: string };
}

export default async function ProfilePage({ params }: Params) {
  const users = await apiFetch<User[]>("/users");
  const user = users.find((u) => u.username === params.username);
  if (!user) {
    return <p>User not found.</p>;
  }
  return (
    <Card>
      <CardContent className="space-y-2">
        <h1 className="text-3xl font-semibold">{user.username}</h1>
        <p className="text-slate-600">{user.bio ?? "Local neighbor"}</p>
        <div className="text-sm text-slate-500">
          <p>Email: {user.email}</p>
          <p>Location: {user.location ?? "SE22"}</p>
        </div>
      </CardContent>
    </Card>
  );
}
