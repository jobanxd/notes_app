# Use an official Python image
FROM python:3.11-slim

# Set workdir
WORKDIR /app

# Install psycopg2 dependencies
RUN apt-get update && apt-get install -y build-essential libpq-dev gcc

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY ./src ./src

# Run the app
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
