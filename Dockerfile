FROM python:3.7

RUN mkdir /api-client
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY pull_account_data.py /api-client
COPY account_traffic_report.py /api-client
COPY main.py /api-client

WORKDIR /api-client

CMD /bin/bash
