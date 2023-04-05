# syntax=docker/dockerfile:1

FROM registry.access.redhat.com/ubi8/python-39

WORKDIR /

COPY app/ .

RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt 
    

EXPOSE 5000

ENV AWS_ACCESS_KEY_ID=<your_access_key>
ENV AWS_SECRET_ACCESS_KEY=<your_secret_key>
ENV S3_BUCKET_NAME=qr-generator-bucket

ENTRYPOINT ["python"]
CMD ["main.py"]
