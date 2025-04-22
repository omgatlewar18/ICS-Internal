# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the current files into the container
COPY . /app

# Install dependencies
RUN pip install flask

# Expose the port Flask runs on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
