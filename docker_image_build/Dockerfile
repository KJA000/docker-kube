FROM python:latest
MAINTAINER jiaekim0 "theyummy@khu.ac.kr"
COPY . /jiaekim
RUN apt-get update
RUN mkdir -p /jiaekim
RUN pip3 install flask

CMD ["python", "/jiaekim/firstserver.py"]

EXPOSE 8080
