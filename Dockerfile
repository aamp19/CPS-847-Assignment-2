FROM python:3.6.1
WORKDIR /docker-flask-test
ADD . /docker-flask-test
EXPOSE 5000
CMD ["python","app.py"]
