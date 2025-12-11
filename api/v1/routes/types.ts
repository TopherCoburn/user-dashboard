// types.ts

export interface User {
  id: number;
  name: string;
  email: string;
  password: string;
}

export interface LoginRequest {
  email: string;
  password: string;
}

export interface LoginResponse {
  token: string;
  user: User;
}

export interface DashboardResponse {
  user: User;
  messages: string[];
}

export interface Message {
  id: number;
  text: string;
  read: boolean;
  userId: number;
}

export interface CreateMessageRequest {
  text: string;
}