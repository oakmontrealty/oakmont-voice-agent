# Use official Python runtime as a base image
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port 8080 for Cloud Run
EXPOSE 8080

# Default command to run the FastAPI server via uvicorn
CMD ["uvicorn", "agent:app", "--host", "0.0.0.0", "--port", "8080"]
