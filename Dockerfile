FROM python:3.10-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn" , "-b", "0.0.0.0", "main:app"]
