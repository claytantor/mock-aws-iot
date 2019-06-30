FROM ubuntu:latest
MAINTAINER Clay Graham "claytantor@flashlex.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements-docker.txt
ENTRYPOINT ["python"]
CMD ["mockiot.py"]