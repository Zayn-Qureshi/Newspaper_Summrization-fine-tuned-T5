# Newspaper Summarization Web App

This repository contains a **Flask-based web application** that summarizes newspaper articles or PDFs using a **fine-tuned T5 model**. The project is integrated with **Hugging Face Spaces** for hosting the web app and the model.  

---

## Project Overview

This project allows users to:

- Input newspaper articles as text or upload PDFs.  
- Automatically generate concise summaries using a fine-tuned T5 model.  
- Remove duplicate or near-duplicate sentences in the output for cleaner summaries.  

The project was developed locally in **VS Code**, then deployed to **Hugging Face Spaces** for hosting the web app.  

---

## Project Structure

### Local Folder (`NewspaperSummarization`)
NewspaperSummarization/
│
├─ app.py # Main Flask application
├─ index.html # Web interface (HTML template)
├─ requirements.txt # Python dependencies
├─ fine_tuned_t5/ # Fine-tuned T5 model files (local)
│ ├─ config.json
│ ├─ tokenizer_config.json
│ ├─ spiece.model
│ ├─ added_tokens.json
│ ├─ special_tokens_map.json
│ ├─ model.safetensors
│ └─ generation_config.json

shell
Copy code

### Hugging Face Spaces Repo (`newspaper-summarization-app`)
newspaper-summarization-app/
│
├─ app.py # Flask app, updated to load model from HF hub
├─ index.html # HTML file in root (templates folder not used)
├─ requirements.txt # Dependencies

yaml
Copy code

---

## Model Details

- **Model Architecture:** T5 (`Text-to-Text Transfer Transformer`)  
- **Fine-tuned Task:** Summarization of newspaper articles.  
- **Training Dataset:** Custom newspaper articles dataset.  
- **Hugging Face Model Hub:** The fine-tuned model is uploaded to HF for easy access.  

Example loading in app:
```python
from transformers import T5Tokenizer, T5ForConditionalGeneration

model_repo = "<username>/<model-repo>"
tokenizer = T5Tokenizer.from_pretrained(model_repo)
model = T5ForConditionalGeneration.from_pretrained(model_repo)
Using the Hugging Face hub avoids the need to upload large model files to GitHub.

Web App Features
Flask-based server rendering index.html.

Input text or PDF upload for summarization.

Removes repeated/near-duplicate sentences in the summary.

Displays character count and word count of input.

Works locally and when deployed to Hugging Face Spaces.

Hugging Face Integration
Spaces: Hosts the web app with Flask.

Model Hub: Stores the fine-tuned T5 model.

Important Notes for Spaces Deployment:

Place app.py and index.html in the root folder of the Space.

Set template_folder="." in Flask to load HTML from root.

Load the model from HF hub instead of local folder.

Access the app via the public URL provided by HF Spaces — do not use 127.0.0.1.

Local Setup Instructions
Clone Repo

bash
Copy code
git clone <your-repo-url>
cd NewspaperSummarization
Install Dependencies

bash
Copy code
pip install -r requirements.txt
Run Flask App Locally

bash
Copy code
python app.py
Access Web App

Open browser: http://127.0.0.1:5000

Enter text or upload PDF to generate summaries.

Using the App
Enter newspaper text in the input box OR upload a PDF.

Click Submit.

View the generated summary along with character and word count.

Notes & Considerations
The fine-tuned T5 model is large, so it is recommended to run on a machine with sufficient RAM (~8–16GB).

When deployed to HF Spaces, model files are downloaded automatically from the hub.

Make sure index.html is in the root folder because Spaces does not allow folder creation.

Debug logs are available in the console to track requests and summarization events.

