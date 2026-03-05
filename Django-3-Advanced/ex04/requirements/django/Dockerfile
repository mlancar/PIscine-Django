FROM python:3.10-slim

WORKDIR /d08

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y gettext \
    && rm -rf /var/lib/apt/lists/*

COPY . /d08/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]