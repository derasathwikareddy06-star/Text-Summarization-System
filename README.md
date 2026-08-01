<!-- ...existing code... -->
# Text Summarization System

A concise FastAPI web app that summarizes long text using Hugging Face's BART (facebook/bart-large-cnn) model and saves summaries to output/summary.txt.

## Features
- Single-page FastAPI frontend
- BART-based summarization via transformers pipeline
- Saves latest summary to output/summary.txt
- Simple HTML/CSS/JS UI

## Project structure
```
Text_Summarization_Project 2/
│── app.py
│── summarizer.py
│── requirements.txt
│── README.md
│── static/
│   ├── style.css
│   └── script.js
│── templates/
│   └── index.html
│── output/
│   └── summary.txt
```

## Setup (Windows)
1. Clone repo:
```powershell
git clone https://github.com/YOUR_USERNAME/Text_Summarization_Project.git
cd "C:\Text_Summarization_Project 2"
```
2. Create & activate venv:
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1   # or .venv\Scripts\activate for cmd
```
3. Install deps:
```powershell
pip install -r requirements.txt
```

## Run
```powershell
uvicorn app:app --reload
```
Open: http://127.0.0.1:8000

## Notes
- Ensure output/ exists and is writable.
- Large models require sufficient RAM/GPU; consider smaller models for low-resource machines.
- To change model, edit summarizer.py pipeline model name.

## Author
Sathwika Reddy
