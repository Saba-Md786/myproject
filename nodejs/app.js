// Load Express module
const express = require('express');
const app = express();

// Set the port inside the container
const PORT = 3000;

// Simple route to show content
app.get('/', (req, res) => {
    res.send(`
        <h1>Hello from Node.js inside Docker!</h1>
        <p>This is a simple web app running in a container.</p>
        <p>Change this content on host, and it will reflect in the container if volume is mapped!</p>
    `);
});

// Start the server
app.listen(PORT, '0.0.0.0', () => {
    console.log(`Server is running on port ${PORT}`);
});

