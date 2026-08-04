from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
import uvicorn

from summarizer import summarize_text

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "request": request,
            "summary": "",
            "text": ""
        }
    )

@app.get("/{path:path}", response_class=HTMLResponse)
async def catch_all(request: Request, path: str):
    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "request": request,
            "summary": "",
            "text": ""
        }
    )

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)

@app.post("/summarize", response_class=HTMLResponse)
async def summarize(request: Request, text: str = Form(...)):
    summary = summarize_text(text)

    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "request": request,
            "summary": summary,
            "text": text
        }
    )