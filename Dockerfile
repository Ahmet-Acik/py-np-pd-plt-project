# Dockerfile for Python Data Science Tutorial

FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
COPY tests/requirements.txt ./tests/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir -r tests/requirements.txt

# Copy the rest of the application
COPY . .

# Expose port for Flask app
EXPOSE 5000

# Default command: run a simple script
CMD ["python", "main/src/01_hello.py"]