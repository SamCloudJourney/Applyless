export interface User {
  id: string;
  username: string;
  email: string;
  avatar_url?: string;
}

export interface Thread {
  id: string;
  title: string;
  category_id: string;
  tags?: string;
  trusted_score?: number;
  created_at: string;
  author?: User;
}

export interface Post {
  id: string;
  thread_id: string;
  content: string;
  created_at: string;
  updated_at: string;
  author?: User;
}

export interface Category {
  id: string;
  name: string;
  description?: string;
  slug: string;
}

export interface Notification {
  id: string;
  type: string;
  data: Record<string, unknown>;
  is_read: boolean;
  created_at: string;
}
