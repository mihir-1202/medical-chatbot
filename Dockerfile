# Use official Python 3.10 slim image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /backend

# Copy requirements first for caching
COPY ./backend/requirements.backend.txt ./requirements.txt

# Upgrade pip and install dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r ./requirements.txt

# Copy your application code
COPY ./backend/ /backend

# Change to app directory where main.py is
WORKDIR /backend/app

# Expose the port your app will run on
EXPOSE 8000

# Command to run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
