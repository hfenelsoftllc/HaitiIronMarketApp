FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
#RUN apt-get update && apt-get install -y --no-install-recommends mysqlclient && rm -rf /var/lib/apt/lists/*
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

#RUN chmod u+x ./entrypoint.sh
#ENTRYPOINT ["./entrypoint.sh"]
CMD python mainapp.py