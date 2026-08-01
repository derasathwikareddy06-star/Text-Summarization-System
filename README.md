# Text Summarization System

A simple AI-powered Text Summarization web application built using FastAPI and Hugging Face Transformers. This application summarizes long text into a concise summary using the BART (facebook/bart-large-cnn) model.

## Features

- Summarizes long text automatically
- User-friendly web interface
- FastAPI backend
- Hugging Face Transformers (BART model)
- Saves generated summaries to `output/summary.txt`

## Technologies Used

- Python
- FastAPI
- Hugging Face Transformers
- Torch
- Jinja2
- HTML
- CSS
- JavaScript

## Project Structure

```
Text_Summarization_Project/
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

## Installation

1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Text_Summarization_Project.git
```

2. Move to the project folder

```bash
cd Text_Summarization_Project
```

3. Create a virtual environment

```bash
python -m venv .venv
```

4. Activate the virtual environment

Windows:

```bash
.venv\Scripts\activate
```

5. Install dependencies

```bash
pip install -r requirements.txt
```

## Run the Project

```bash
uvicorn app:app --reload
```

Open your browser and visit:

```
http://127.0.0.1:8000
```

## Example

Enter a paragraph of text and click **Summarize**.

The generated summary will be displayed on the webpage and also saved in:

```
output/summary.txt
```

## Future Enhancements

- File upload support
- PDF summarization
- Download summary as PDF
- Multiple language support
- Streamlit deployment

## Author

Sathwika Reddy