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
    "dag_id": "2-xcoms",
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

@task
def push_task(**context):
    context['ti'].xcom_push(key='mensaje', value='Hola desde el PUSH!')


@task
def pull_task(**context):
    mensaje = context['ti'].xcom_pull(task_ids='push_task', key='mensaje')
    print(f"Mensaje recibido: {mensaje}")


@dag(**dag_parameters)
def etl_pipeline():
    start = start_dag()

    push_xcom = push_task()
    
    pull_xcom = pull_task()

    end = end_dag()

    start >> push_xcom >> pull_xcom  >> end

dag = etl_pipeline()
