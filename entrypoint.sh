#!/usr/bin/env bash


airflow db init && airflow users  create --role Admin --username airflow --email admin --firstname admin --lastname admin --password airflow
/entrypoint webserver