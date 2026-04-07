// backend/server.js
const express = require('express');
const { body, validationResult } = require('express-validator');
const helmet = require('helmet');
const bcrypt = require('bcrypt');
const cors = require('cors');

const app = express();

// SECURITY MIDDLEWARE
app.use(cors()); // Allows your React app to talk to this server
app.use(express.json()); // Lets server read JSON data
app.use(helmet()); // Sets secure HTTP headers to block XSS

// Mock Database (In a real app, this is your SQL database)
const users = [
  { email: "user@test.com", passwordHash: "$2b$10$K9p..example..hash" } 
];

app.post('/api/login', [
  // 1. VALIDATION & XSS PREVENTION
  body('email').isEmail().normalizeEmail(),
  body('password').isLength({ min: 8 }).trim().escape()
], async (req, res) => {
  
  const errors = validationResult(req);
  if (!errors.isEmpty()) return res.status(400).json({ error: "Invalid data" });

  const { email, password } = req.body;

  try {
    // 2. PREVENT SQL INJECTION
    // In a real DB, use: await db.query('SELECT * FROM users WHERE email = $1', [email])
    const user = users.find(u => u.email === email);

    if (!user) return res.status(401).json({ error: "Access Denied" });

    // 3. SECURE PASSWORD CHECK
    const isMatch = await bcrypt.compare(password, user.passwordHash);
    if (!isMatch) return res.status(401).json({ error: "Access Denied" });

    res.json({ success: true, message: "Securely Logged In!" });

  } catch (err) {
    res.status(500).send("Server Error");
  }
});

app.listen(5000, () => console.log('Server running on port 5000'));