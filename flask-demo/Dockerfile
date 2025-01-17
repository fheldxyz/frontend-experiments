FROM python:3.9-alpine

WORKDIR /app
COPY app.py /app/
COPY static/index.html /app/static/

RUN pip install flask gunicorn

EXPOSE 5000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]

