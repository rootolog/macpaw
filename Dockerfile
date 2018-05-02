FROM macpaw/internship
MAINTAINER Volodymyr Gedz "rootolog@gmail.com"
RUN apt-get update && apt-get install -y zip logrotate vim
RUN mv /app/main.py /app/wrong.py 
CMD [ "uwsgi", "--socket", "0.0.0.0:8080", \
               "--uid", "uwsgi", \
               "--plugins", "python3", \
               "--protocol", "uwsgi", \
               "--wsgi", "main:application" ]
