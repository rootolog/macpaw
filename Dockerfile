FROM macpaw/internship
MAINTAINER Volodymyr Gedz "rootolog@gmail.com"
RUN apt-get update && apt-get install -y zip logrotate

COPY main.py /app

RUN rm /app/uwsgi.ini
COPY uwsgi.ini /app

RUN rm /etc/nginx/conf.d/nginx.conf
COPY nginx.conf /etc/nginx/conf.d/ 

#RUN rm /etc/logrotate.d/supervisor
#COPY supervisor /etc/logrotate.d/

#CMD ["chmod", "+x", "/app/cron.sh", "&", "sh" "/app/cron.sh"]
