from transformers import T5ForConditionalGeneration, T5Tokenizer

# Hugging Face repo path
model_name = "Zain78877/NewspaperSummrization"

# Load tokenizer and model
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# Optional: test summary
def summarize(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    summary_ids = model.generate(**inputs)
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

if __name__ == "__main__":
    text = "summarize: This is a long news article you want to summarize."
    print("Summary:", summarize(text))
