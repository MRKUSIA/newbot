# Обзор контейнера
FROM python:3.11 alpine

#Рабочая папка
WORKDIR /app

#Копируем зависимости
COPY req.txt .

RUN pip install --no--cache-dir -r req.txt

COPY . .
CMD ["python3", "main.py"]
