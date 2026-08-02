from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="Falconsai/text_summarization"

def summarize_text(text):
    result= summarizer(
        text,
        max_length=100,
        min_length=30,
        do_sample=False
    )
    summary=result[0]["summary_text"]
# Save summary 
    with open("output/summary.txt", "w", encoding="utf-8") as file:
        file.write(summary)

    return summary