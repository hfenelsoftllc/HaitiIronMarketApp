FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
#RUN apt-get update && apt-get install -y --no-install-recommends mysqlclient && rm -rf /var/lib/apt/lists/*
COPY requirement.txt /app/requirement.txt
RUN pip install --no-cache-dir -r requirement.txt
COPY . .


EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]