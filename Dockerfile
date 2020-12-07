FROM python:3-alpine3.12
COPY . /app
COPY root /var/spool/cron/crontabs/root
WORKDIR /app
RUN pip3 install -r requirements.txt
RUN chmod +x /app/main.py
CMD crond -l 2 -f