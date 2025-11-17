"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { api } from "../../../lib/api-client";
import { Input } from "../../../components/ui/input";
import { Button } from "../../../components/ui/button";

export default function RegisterPage() {
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    try {
      await api.post("/auth/register", { email, username, password });
      router.push("/auth/login");
    } catch (err) {
      setError("Unable to register. Try a different email/username.");
      console.error(err);
    }
  }

  return (
    <div className="max-w-md mx-auto space-y-4">
      <h1 className="text-3xl font-semibold">Create your account</h1>
      <form className="space-y-3" onSubmit={handleSubmit}>
        <Input value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Email" type="email" required />
        <Input value={username} onChange={(e) => setUsername(e.target.value)} placeholder="Username" required />
        <Input value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" type="password" required />
        {error && <p className="text-sm text-red-500">{error}</p>}
        <Button className="w-full" type="submit">
          Sign up
        </Button>
      </form>
    </div>
  );
}
