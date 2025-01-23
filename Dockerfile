FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
COPY .env .

# Define the entry point
CMD ["python", "app.py"]