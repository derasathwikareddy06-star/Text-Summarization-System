from pathlib import Path

from transformers import pipeline

MODEL_NAME = "facebook/bart-large-cnn"

try:
    summarizer = pipeline("summarization", model=MODEL_NAME)
except KeyError:
    summarizer = pipeline("text2text-generation", model=MODEL_NAME)


def summarize_text(text: str) -> str:
    result = summarizer(
        text,
        max_length=100,
        min_length=30,
        do_sample=False,
    )
    summary = result[0].get("summary_text") or result[0].get("generated_text") or ""

    output_path = Path("output")
    output_path.mkdir(parents=True, exist_ok=True)
    with open(output_path / "summary.txt", "w", encoding="utf-8") as file:
        file.write(summary)

    return summary