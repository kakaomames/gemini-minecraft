FROM openjdk:21-slim
RUN apt-get update && apt-get install -y python3
WORKDIR /app
COPY . .
EXPOSE 8080
CMD ["python3", "main.py"]