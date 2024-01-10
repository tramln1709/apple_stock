FROM centos/python-38-centos7
USER root


WORKDIR /usr/app/data_process

COPY requirements.txt .
RUN pip install --upgrade pip \
    pip install -r requirements.txt

COPY src .

WORKDIR /usr/app/data_process/stock_analyzer

CMD ["python", "process.py"]