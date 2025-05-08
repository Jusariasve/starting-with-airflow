import json

from datetime import datetime, timedelta

from airflow.decorators import dag, task
from airflow.models.variable import Variable
from airflow.providers.amazon.aws.operators.lambda_function import LambdaInvokeFunctionOperator

from params import PARAMS


# --- Default args ---
default_args = {
    "owner": "data-team",
    "retries": 1,
    "retry_delay": timedelta(seconds=10),
}

dag_parameters = {
    "dag_id": "4-agregar_operadores",
    "default_args": default_args,
    "start_date": datetime(2025, 1, 1),
    "schedule": "0 0 1 4,9 *", # Abril y Septiembre el primer dia, a las 00:00
    "catchup": False,
    "params": PARAMS,
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

@task
def obtener_params(**context):
    nombre = context.get("params").get("nombre_ejecutor")
    print(f"Dag ejecutado por: {nombre}")

@task
def sumar_resultados(**context):
    res1 = context["ti"].xcom_pull(task_ids="lambda_call_juan")
    res2 = context["ti"].xcom_pull(task_ids="lambda_call_sebas")

    # Extraer el valor de 'body.value'
    val1 = json.loads(json.loads(res1)["body"])["value"]
    val2 = json.loads(json.loads(res2)["body"])["value"]

    resultado = val1 + val2
    print(f"La suma de los valores es: {resultado}")
    return resultado


@dag(**dag_parameters)
def etl_pipeline():
    start = start_dag()

    consultar_params = obtener_params()

    push_xcom = push_task()
    
    pull_xcom = pull_task()

    nombre_lambda = Variable.get("nombre_lambda_test")
    payload = json.dumps({"name": "juan", "value": 10})
    elevar_primer_param = LambdaInvokeFunctionOperator(
        task_id=f"lambda_call_juan",
        function_name=nombre_lambda,
        payload=payload,
        aws_conn_id="aws_default",
        region_name="us-east-1",
    )
    payload = json.dumps({"name": "sebas", "value": 5})
    elevar_segundo_param = LambdaInvokeFunctionOperator(
        task_id=f"lambda_call_sebas",
        function_name=nombre_lambda,
        payload=payload,
        aws_conn_id="aws_default",
        region_name="us-east-1",
    )

    sumar_respuestas_lambda = sumar_resultados()

    end = end_dag()

    start >> consultar_params >> push_xcom >> pull_xcom >> [elevar_primer_param, elevar_segundo_param] >> sumar_respuestas_lambda >> end

dag = etl_pipeline()
