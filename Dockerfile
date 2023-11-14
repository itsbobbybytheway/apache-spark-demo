FROM bitnami/spark:3.0.0
WORKDIR /app
COPY . /app
CMD ["spark-submit", "app.py"]