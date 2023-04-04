# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
COPY . /app
WORKDIR /app

RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt 
    
COPY . /app

#ENV AWS_ACCESS_KEY_ID=<your-access-key-id>
#ENV AWS_SECRET_ACCESS_KEY=<your-secret-access-key>
#ENV S3_BUCKET_NAME=<your-bucket-name>

ENTRYPOINT ["python"]
CMD ["local.py"]
