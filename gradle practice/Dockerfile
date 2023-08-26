FROM openjdk:8-jre-alpine
WORKDIR /app
COPY ./build/libs/app.jar .
EXPOSE 8001
CMD java -jar app.jar