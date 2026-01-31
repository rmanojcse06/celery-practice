# Use Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask port
EXPOSE 5000

# Default command to run Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
