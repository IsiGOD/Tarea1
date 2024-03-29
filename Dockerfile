FROM python:3.9

WORKDIR /app

COPY requirements.txt .

COPY app.py .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["python", "app.py"]