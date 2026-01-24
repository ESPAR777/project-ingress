# Use the official Python image
FROM python:3.12-slim

# Set environment variables to prevent Python from writing .pyc files 
# and to ensure output is sent straight to terminal
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Install dependencies
# We copy this first to leverage Docker's cache
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . /app/

# Expose the port Django runs on
EXPOSE 8000

# Start the Django server
# 0.0.0.0 is required to allow external access to the container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]