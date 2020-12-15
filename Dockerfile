FROM python:3.7-slim
WORKDIR /app
COPY app.py requirements.txt test_app.py /app/
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python3", "app.py"]
