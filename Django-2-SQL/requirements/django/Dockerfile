FROM python:3.10-slim

WORKDIR /d42

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y postgresql-client


COPY . /d42/

WORKDIR /d42/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]