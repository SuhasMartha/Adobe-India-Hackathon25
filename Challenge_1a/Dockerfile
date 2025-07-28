FROM --platform=linux/amd64 python:3.10

WORKDIR /app

COPY extract_outline.py .
COPY Inputs ./Inputs
COPY Outputs ./Outputs

RUN pip install pymupdf

CMD ["python", "extract_outline.py"]

# ============================
# Stage 1: Base Image
# ============================
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy Challenge 1A files into container
COPY Challenge_1a/ /app/Challenge_1a/

# Install dependencies
RUN pip install --no-cache-dir -r Challenge_1a/requirements.txt

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Default command to run outline extraction
CMD ["python", "Challenge_1a/utils/extract_outline.py", "Challenge_1a/Inputs/file01.pdf"]
