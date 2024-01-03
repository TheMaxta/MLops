# backend/Dockerfile

# Base Python image
FROM python:3.8

# Set working directory
WORKDIR /app

# Install Java Runtime
RUN apt-get update && apt-get install -y default-jre

# Copy requirements file
COPY requirements-backend.txt requirements.txt

# Install Python packages
RUN pip install -r requirements.txt

# Copy application code
COPY . /app

# Expose port 8000
EXPOSE 8000

# Start Uvicorn server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
