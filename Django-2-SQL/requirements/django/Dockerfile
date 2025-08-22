FROM python:3.10-slim

WORKDIR /d42

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src .

WORKDIR /d42/d42/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]