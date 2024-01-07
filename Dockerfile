FROM spark:3.5.0-scala2.12-java17-ubuntu

USER root

RUN set -ex; \
    apt-get update; \
    apt-get install -y python3 python3-pip; \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /usr/app/apple_interview/requirements.txt
RUN pip install --upgrade pip;\
    pip install -r /usr/app/apple_interview/requirements.txt

WORKDIR /usr/app/apple_interview

COPY . .

CMD ["python3", "process.py"]