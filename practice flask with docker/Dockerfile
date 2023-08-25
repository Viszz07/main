FROM python:3.8.1-alpine
WORKDIR /app
COPY  app.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5005
CMD python app.py


