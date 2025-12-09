from transformers import T5Tokenizer, T5ForConditionalGeneration

# 1. Use your new repo name
repo_name = "Zain78877/news_summarizer_t5"

# 2. Path to your local fine-tuned model folder
model_path = r"C:\Users\HP\PycharmProjects\newspaper_summrization\fine_tuned_t5"

# 3. Load and push
model = T5ForConditionalGeneration.from_pretrained(model_path)
tokenizer = T5Tokenizer.from_pretrained(model_path)

model.push_to_hub(repo_name)
tokenizer.push_to_hub(repo_name)

print(f"✅ Uploaded to https://huggingface.co/{repo_name}")
