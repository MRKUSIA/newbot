FROM python:3.13-alpine

WORKDIR /app

COPY req.txt .

RUN pip install --no-cache-dir -r req.txt

COPY . .

CMD ["python3", "main.py"]