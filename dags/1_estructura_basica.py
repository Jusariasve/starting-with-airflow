import json

from datetime import datetime, timedelta

from airflow.decorators import dag, task


# --- Default args ---
default_args = {
    "owner": "data-team",
    "retries": 1,
    "retry_delay": timedelta(seconds=10),
}

dag_parameters = {
    "dag_id": "1-estructura_basica",
    "default_args": default_args,
    "start_date": datetime(2025, 1, 1),
    "schedule": "0 0 1 4,9 *", # Abril y Septiembre el primer dia, a las 00:00
    "catchup": False,
    "tags": ["etl", "lambda", "test"],
}


@task
def start_dag(**context):
    dag_id = context["dag"].dag_id
    print(f"Inicio del DAG: {dag_id}")

@task
def end_dag():
    print("Fin del DAG")


@dag(**dag_parameters)
def etl_pipeline():
    start = start_dag()
    end = end_dag()

    start >> end

dag = etl_pipeline()
