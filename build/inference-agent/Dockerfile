
FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    wget \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .
COPY squeezenet1.1-7.onnx .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
