FROM python:3.8

WORKDIR .

COPY requirements.txt requirements.txt

RUN python -m venv venv && pip install -r requirements.txt

COPY src src

COPY app.py app.py

CMD ["python", "app.py", "--host", "0.0.0.0"]