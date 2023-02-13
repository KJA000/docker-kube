FROM docker.io/python:3.9.15
RUN apt-get update
WORKDIR /me
COPY server.py .
EXPOSE 65456
CMD ["python", "/me/server.py"]