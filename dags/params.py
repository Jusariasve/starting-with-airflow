from airflow.models.param import Param

PARAMS = {
    "nombre_ejecutor": Param(
        default="Test",
        description="Nombre de la persona que ejecuta el DAG",
        type="string",
    ),
}
