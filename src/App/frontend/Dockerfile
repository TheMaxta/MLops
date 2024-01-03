# frontend/Dockerfile

# Base Python image
FROM python:3.8

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements-frontend.txt requirements.txt

# Install Python packages
RUN pip install -r requirements.txt

# Copy application code
COPY . /app

# Expose port 8501
EXPOSE 8501

# Start Streamlit app
CMD ["streamlit", "run", "app.py"]
