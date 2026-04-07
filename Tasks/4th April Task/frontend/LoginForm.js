// frontend/src/LoginForm.js
import React, { useState } from 'react';

function LoginForm() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [msg, setMsg] = useState('');

  const handleLogin = async (e) => {
    e.preventDefault();
    
    const res = await fetch('http://localhost:5000/api/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password })
    });

    const data = await res.json();
    setMsg(data.success ? data.message : data.error);
  };

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h2>Secure Login</h2>
      <form onSubmit={handleLogin}>
        <input type="email" placeholder="Email" onChange={e => setEmail(e.target.value)} required /><br/>
        <input type="password" placeholder="Password" onChange={e => setPassword(e.target.value)} required /><br/>
        <button type="submit">Login</button>
      </form>
      <p>{msg}</p>
    </div>
  );
}

export default LoginForm;