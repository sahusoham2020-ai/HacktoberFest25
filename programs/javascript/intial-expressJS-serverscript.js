const express = require('express');

const app = express();
const PORT = 3001;

// Middleware to parse JSON bodies
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Logging middleware
app.use((req, res, next) => {
  console.log(`${req.method} ${req.url}`);
  next();
});

// Routes
app.get('/', (req, res) => {
  res.send('<h1>Welcome to Express Server!</h1>');
});

app.get('/about', (req, res) => {
  res.send('<h1>About Page</h1><p>This is an Express.js server.</p>');
});

app.get('/api/data', (req, res) => {
  res.json({
    message: 'Hello from the API!',
    timestamp: new Date().toISOString()
  });
});

// POST route example
app.post('/api/submit', (req, res) => {
  const data = req.body;
  res.json({
    success: true,
    received: data
  });
});

// 404 handler
app.use((req, res) => {
  res.status(404).send('<h1>404 - Page Not Found</h1>');
});

// Start server
app.listen(PORT, () => {
  console.log(`Express server running at http://localhost:${PORT}/`);
});