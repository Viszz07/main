FROM python:alpine3.7
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN pip install pytest
RUN pytest test_app.py 
EXPOSE 5000
CMD python app.py

