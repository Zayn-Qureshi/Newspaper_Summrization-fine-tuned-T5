import os
from flask import Flask, render_template, request
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration
import PyPDF2  # New import for PDF handling
import re
import difflib
from load_model import model, tokenizer, summarize

text = "summarize: Your news article goes here..."
summary_text = summarize(text)
print(summary_text)

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), "templates"))

# Load the fine-tuned model
model_path = "./fine_tuned_t5"
tokenizer = T5Tokenizer.from_pretrained(model_path)
model = T5ForConditionalGeneration.from_pretrained(model_path)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()


def summarize_text(input_text):
    """Generates a summary for the given input text."""
    if not input_text or not input_text.strip():
        return None

    inputs = tokenizer(
        input_text,
        return_tensors="pt",
        max_length=512,
        truncation=True
    )
    inputs = {k: v.to(device) for k, v in inputs.items()}

    # Generate summary
    with torch.no_grad():
        summary_ids = model.generate(
            inputs["input_ids"],
            attention_mask=inputs.get("attention_mask"),
            max_length=128,
            num_beams=4,
            early_stopping=True
        )
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    # remove accidental repeated/near-duplicate sentences produced by the model
    summary = _dedupe_near_duplicate_sentences(summary)

    # normalize whitespace
    summary = re.sub(r'\s+', ' ', summary).strip()

    return summary


def _dedupe_near_duplicate_sentences(text, similarity_threshold=0.85):
    """
    Split text into sentences and remove consecutive sentences that are near-duplicates.
    Uses a simple similarity check (difflib.SequenceMatcher). Keeps order.
    """
    if not text or not text.strip():
        return text or ""

    # split on sentence boundaries (keeps punctuation)
    sentences = re.split(r'(?<=[\.\?\!])\s+', text.strip())
    out = []
    prev = None
    for s in sentences:
        s_clean = s.strip()
        if not s_clean:
            continue
        if prev is not None:
            # similarity ratio between previous and current sentence
            ratio = difflib.SequenceMatcher(None, prev.lower(), s_clean.lower()).ratio()
            if ratio >= similarity_threshold:
                # skip this sentence as it's essentially a repeat of the previous
                continue
        out.append(s_clean)
        prev = s_clean
    return " ".join(out)


def extract_text_from_pdf(pdf_file):
    """Extracts text from a PDF file."""
    text = ""
    with open(pdf_file, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text.strip()


@app.route("/", methods=["GET", "POST"])
def index():
    context = {
        'input_text': request.form.get("input_text", ""),
        'summary': None,
        'char_count': 0,
        'word_count': 0
    }

    if request.method == "POST":
        input_text = request.form.get("input_text", "")
        pdf_file = request.files.get("pdf_file")

        if pdf_file:
            input_text = extract_text_from_pdf(pdf_file)

        if input_text:
            context['input_text'] = input_text
            context['summary'] = summarize_text(input_text)
            context['char_count'] = len(input_text)
            context['word_count'] = len(input_text.split())

    # log what will be rendered so you can confirm rendering happens on the server
    app.logger.info("Rendering index.html with context: input_text length=%d, summary set=%s",
                    len(context.get('input_text') or ""), bool(context.get('summary')))

    return render_template("index.html", **context)


if __name__ == "__main__":
    app.run(debug=True)
