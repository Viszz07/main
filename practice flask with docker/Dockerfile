FROM python:3.8.1-alpine
WORKDIR /app
COPY  . .
RUN pip install -r requirements.txt
RUN pip install pytest
EXPOSE 5005
CMD python app.py


