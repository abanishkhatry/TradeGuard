import React from "react";
import { useState } from "react";
import { registerUser } from "../api/auth";
import { Button } from "../components/ui/button";
import { Input } from "../components/ui/input";

export default function Register() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setError("");
    setSuccess("");

    try {
      // Call the registerUser function from the auth API to register the user.
      const data = await registerUser(email, password);
      setSuccess("Account created! Redirecting to login...");
      setTimeout(() => {
        window.location.href = "/login";
      }, 1500);
    } catch (err: any) {
      setError(err.message);
    }
  }

  return (
    <div className="h-screen flex items-center justify-center">
      <form
        onSubmit={handleSubmit}
        className="p-6 w-[350px] border rounded-xl shadow-lg flex flex-col gap-3"
      >
        <h1 className="text-xl font-bold text-center">Create Account</h1>

        {error && <p className="text-red-600 text-sm text-center">{error}</p>}
        {success && <p className="text-green-600 text-sm text-center">{success}</p>}

        <Input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />

        <Input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <Button type="submit" className="w-full">
          Register
        </Button>
      </form>
    </div>
  );
}
