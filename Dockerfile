FROM python:3.10-slim

WORKDIR /app

# Install git and system dependencies potentially needed for lighter builds
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Install PyTorch CPU-only (Much smaller: ~200MB vs 2GB+)
RUN pip install --no-cache-dir torch torchvision --index-url https://download.pytorch.org/whl/cpu

# Copy requirements
COPY requirements.txt .

# Install other dependencies (transformers, etc.)
# We explicitly allow looking at the extra index but prefer standard PyPI for others
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
