FROM python:3.8

WORKDIR /url-shortener

COPY requirements.txt .

RUN pip install -r requirements.txt

ENV NAME venv

COPY . .

CMD ["python", "app.py"]

