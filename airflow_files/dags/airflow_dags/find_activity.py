import os
import sys

sys.path.append("..")
SCRIPTS_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPTS_DIR, '..')))

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
from scripts import campaign_get_activity_data

# @dag(schedule_interval='@daily',
#      start_date=datetime(2024, 1, 1),
#      tags=['activity'],
#      catchup=False, )
# def find_activity():
#     @task
#     def get_activity():
#         r = requests.get(API)
#         return response.json()
#
#     get_activity()
#
#
# find_activity()
with DAG(
    dag_id='find_activity',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    tags=['activity'],
    catchup=False
) as dag:

    get_activity = PythonOperator(
        task_id='get_activity',
        python_callable=campaign_get_activity_data.campaign_get_activity_data
    )
    get_activity
 # Return the parsed JSON response
