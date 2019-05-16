FROM python:3.6

EXPOSE 5001

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

ADD app /app
CMD ["python", "app.py"]