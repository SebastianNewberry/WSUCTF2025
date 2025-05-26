// src/app.js
const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql');
const path = require('path');
const app = express();
const PORT = 3000;

// Database Connection
const db = mysql.createConnection({
    host: '127.0.0.1',
    user: 'WSUuser',
    password: 'WayneStateUniversity',
    database: 'ctfdb'
});

db.connect(err => {
    if (err) throw err;
    console.log('Connected to database');
});

// Middleware
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

// Routes
app.get('/', (req, res) => {
    res.render('login');
});

app.post('/login', (req, res, next) => {
    const { username, password } = req.body;
    const query = `SELECT * FROM users WHERE username = '${username}' AND password = '${password}'`;
    
    db.query(query, (err, result) => {
        if (err) return next(err);
        if (result.length > 0) {
            res.sendFile(__dirname + '/views/flag.txt');  // Shows the flag if SQLi works
        } else {
            res.send('Login failed. Try again.');
        }
    });
});

app.use((err, req, res, next) => {
    console.error(err);
  
    const status = err.status || 500;
    const message = err.message || 'Internal Server Error';
  
    res.status(status).send(message);
  });

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
