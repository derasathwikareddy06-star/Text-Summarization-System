const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');
const { spawn } = require('child_process');
const path = require('path');

const PY_CMD = process.env.PYTHON || 'python';

console.log('Starting Python backend...');
const py = spawn(PY_CMD, ['-m', 'uvicorn', 'app:app', '--host', '127.0.0.1', '--port', '5000'], { stdio: 'inherit' });

py.on('exit', (code) => {
  console.log(`Python backend exited with code ${code}`);
});

const app = express();

app.use('/static', express.static(path.join(__dirname, 'static')));
app.use('/output', express.static(path.join(__dirname, 'output')));

app.use('/api', createProxyMiddleware({
  target: 'http://localhost:5000',
  changeOrigin: true,
  pathRewrite: {'^/api': ''},
}));

app.use('/', createProxyMiddleware({
  target: 'http://localhost:5000',
  changeOrigin: true,
}));

const DEFAULT_PORT = Number(process.env.PORT || 3000);
let port = DEFAULT_PORT;

const startServer = () => {
  const server = app.listen(port, () => {
    console.log(`Dev server running at http://localhost:${port}`);
  });

  server.on('error', (err) => {
    if (err.code === 'EADDRINUSE') {
      const nextPort = port + 1;
      console.warn(`Port ${port} is already in use. Trying port ${nextPort} instead...`);
      port = nextPort;
      startServer();
    } else {
      throw err;
    }
  });
};

startServer();
