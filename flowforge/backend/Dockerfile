# Lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements for caching speed
COPY requirements.txt .

# Install dependancies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app code
COPY . .

# Run the app using the host 0.0.0.0 so we can listen to outside requests
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]