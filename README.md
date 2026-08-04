# Text Summarization System

A responsive FastAPI web app that summarizes text using Hugging Face's BART model and saves the latest result in `output/summary.txt`.

## Features
- Responsive, styled UI with modern cards and button visuals
- FastAPI backend with Jinja2 template rendering
- Summarization using `facebook/bart-large-cnn`
- Saves each summary to `output/summary.txt`
- Local dev proxy support via `server.js`

## Project structure
```
Text_Summararization_Project 2/
│── app.py
│── summarizer.py
│── requirements.txt
│── package.json
│── README.md
│── server.js
│── vercel.json
│── api/
│   └── index.py
│── static/
│   ├── script.js
│   └── style.css
│── templates/
│   └── index.html
│── output/
│   └── summary.txt
```

## Setup (Windows)
1. Open the project folder:
```powershell
cd "C:\Text_Summarization_Project 2"
```
2. Create and activate a virtual environment:
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```
3. Install Python dependencies:
```powershell
pip install -r requirements.txt
```
4. Install Node dependencies:
```powershell
npm install
```

## Run locally
There are two options:

### Option 1: Use the Node proxy server
```powershell
npm run dev
```
Open: `http://localhost:3000`

If port `3000` is already in use, start on the next available port or set a manual port:
```powershell
$env:PORT=3001; npm run dev
```
or in cmd.exe:
```cmd
set PORT=3001&& npm run dev
```

### Option 2: Run FastAPI directly
```powershell
uvicorn app:app --reload --host 127.0.0.1 --port 5000
```
Open: `http://127.0.0.1:5000`

## Deploy
### Vercel
This project includes `api/index.py` and `vercel.json` so it can deploy as a Python serverless function.

1. Install Vercel CLI:
```powershell
npm install -g vercel
```
2. Deploy:
```powershell
vercel
```

> Note: Large Hugging Face models may exceed serverless limits. For production, consider deploying to a VM or container with enough RAM.

### Docker
Build and run locally with Docker:
```powershell
docker build -t text-summarizer .
docker run --rm -p 8000:8000 text-summarizer
```
Open: `http://127.0.0.1:8000`

## Notes
- Make sure `output/` exists and is writable.
- If the app loads slowly, the model may still be downloading. Wait for the first generation to complete.
- To change the summarization model, update `MODEL_NAME` in `summarizer.py`.

## Styling
The app now uses a responsive dark gradient layout with a polished form and summary card.

## Author
Sathwika Reddy
