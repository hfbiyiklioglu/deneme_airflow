FROM apache/airflow:2.8.1-python3.8
COPY requirements.txt /opt/airflow/
RUN pip install -r requirements.txt
