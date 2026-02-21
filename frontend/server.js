const express = require('express');
const path = require('path');
const fetch = require('node-fetch');

const app = express();
const PORT = 3000;

// Middleware
app.use(express.static('public'));
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// Set view engine
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

const BACKEND_URL = process.env.BACKEND_URL || 'http://localhost:5000';

// Routes
app.get('/', (req, res) => {
  res.render('index', { title: 'Form Submission App' });
});

app.post('/submit', async (req, res) => {
  try {
    const { name, email, message } = req.body;

    if (!name || !email || !message) {
      return res.status(400).render('index', {
        title: 'Form Submission App',
        error: 'All fields are required',
        formData: { name, email, message }
      });
    }

    // Send to Flask backend
    const response = await fetch(`${BACKEND_URL}/api/submit`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ name, email, message })
    });

    const data = await response.json();

    if (data.success) {
      res.render('success', {
        title: 'Success',
        message: `Thank you ${name}! Your message has been received.`,
        submission: data.data
      });
    } else {
      res.status(400).render('index', {
        title: 'Form Submission App',
        error: data.error || 'Failed to submit form',
        formData: { name, email, message }
      });
    }
  } catch (error) {
    console.error('Error:', error);
    res.status(500).render('index', {
      title: 'Form Submission App',
      error: 'Server error: ' + error.message,
      formData: req.body
    });
  }
});

app.get('/submissions', async (req, res) => {
  try {
    const response = await fetch(`${BACKEND_URL}/api/submissions`);
    const data = await response.json();

    res.render('submissions', {
      title: 'All Submissions',
      submissions: data.data || [],
      count: data.count || 0
    });
  } catch (error) {
    console.error('Error:', error);
    res.status(500).render('submissions', {
      title: 'All Submissions',
      submissions: [],
      count: 0,
      error: 'Failed to fetch submissions'
    });
  }
});

app.listen(PORT, '0.0.0.0', () => {
  console.log(`Frontend running on http://0.0.0.0:${PORT}`);
  console.log(`Backend URL: ${BACKEND_URL}`);
});
