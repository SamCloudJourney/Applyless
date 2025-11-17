"use client";

import { useEffect, useState } from "react";
import { api } from "../../lib/api-client";
import { Notification } from "../../types/forum";
import { Card, CardContent, CardHeader } from "../../components/ui/card";

export default function NotificationsPage() {
  const [notifications, setNotifications] = useState<Notification[]>([]);

  useEffect(() => {
    async function load() {
      const { data } = await api.get<Notification[]>("/notifications");
      setNotifications(data);
    }
    load();
  }, []);

  return (
    <div className="space-y-4">
      <h1 className="text-3xl font-semibold">Notifications</h1>
      {notifications.length === 0 && <p className="text-slate-500">No notifications yet.</p>}
      <div className="space-y-3">
        {notifications.map((notification) => (
          <Card key={notification.id}>
            <CardHeader>
              <p className="font-medium">{notification.type}</p>
            </CardHeader>
            <CardContent>
              <pre className="text-sm text-slate-500">{JSON.stringify(notification.data)}</pre>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}
