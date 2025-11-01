# Base image
FROM python:3.13-slim

# Set working directory inside the container
WORKDIR /app

# Copy all files from your local folder to /app in the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir flask pytest

# Expose the Flask port
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "ACEest_Fitness.py"]

