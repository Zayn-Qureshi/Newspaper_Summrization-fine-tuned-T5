# Newspaper Summarization Web App

This project is a **web application** that summarizes newspaper articles or PDFs using a **fine-tuned T5 model**.  

---

## Project Overview

- Summarizes text or PDFs into concise summaries.  
- Removes duplicate or near-duplicate sentences for cleaner output.  
- Developed locally in **VS Code** and deployed to **Hugging Face Spaces** for public access.  

---

## Technologies Used

- **Python**  
- **Flask** – Web framework for the app  
- **PyTorch & Transformers (Hugging Face)** – For T5 model loading and text summarization  
- **PyPDF2** – Extract text from PDFs  
- **HTML/CSS** – Frontend (`index.html`)  

---

## Model Details

- **Architecture:** T5 (Text-to-Text Transfer Transformer)  
- **Training:** Fine-tuned on newspaper articles in **Google Colab**  
- **Deployment:** Model files uploaded to **Hugging Face Hub**, loaded directly in the Space  
- **Advantage:** No need to push large model files to GitHub  

---

## Integration & Deployment

- Flask app renders HTML interface (`index.html`) and handles text/PDF input.  
- Hugging Face Spaces hosts the app and automatically downloads the model from the HF hub.  
- Users access the app via the **Space’s public URL** (no need for `127.0.0.1`).  

---

## Usage

1. Enter text or upload a PDF.  
2. Click **Submit**.  
3. View the generated summary.  

---

**Note:** Make sure `index.html` is in the root folder when deploying to Hugging Face Spaces.  

