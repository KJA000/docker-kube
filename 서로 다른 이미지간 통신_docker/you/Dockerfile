FROM docker.io/python:3.9.15
RUN apt-get update
WORKDIR /you
COPY client.py .
EXPOSE 8080
CMD ["python", "/you/client.py"]