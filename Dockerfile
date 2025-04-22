# Dockerfile

FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Install system dependencies (optional for transformers)
RUN apt-get update && apt-get install -y git

# Copy files into container
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose the port FastAPI will run on
EXPOSE 8000

# Run the app with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]