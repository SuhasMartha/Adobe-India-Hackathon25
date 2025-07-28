# ============================
# Stage 1: Base Image
# ============================
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files into container
COPY Challenge_1b/ /app/Challenge_1b/

# Install dependencies
RUN pip install --no-cache-dir -r Challenge_1b/requirements.txt

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Default command (can be overridden)
CMD ["python", "Challenge_1b/utils/extract_relevant.py", "Challenge_1b/Inputs/Collection 1"]
