FROM python:3.5
MAINTAINER haburibe <haburibe@gmail.com>
ADD main.py /srv
RUN pip install flask
EXPOSE 8080:8080
ENTRYPOINT ["python3", "/srv/main.py"]
