FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN apt-get update && apt-get install -y libaio1 wget unzip gcc libxml2 \
    && cd /app \
    && apt-get update && apt-get install build-essential -y \
    && pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
