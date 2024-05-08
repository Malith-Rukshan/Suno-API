FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install Requirements
RUN pip3 install -U pip
COPY requirements.txt .
RUN pip3 install --no-cache-dir -U -r requirements.txt

# Copying All Source
COPY . .

# Set Port
EXPOSE 8080

# Run API Server
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8080"]