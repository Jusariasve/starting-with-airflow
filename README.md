# 🚀 Empieza con Airflow sin complicaciones!

Este repositorio contiene una colección de DAGs educativos utilizados durante la charla **"Empieza en Airflow sin complicaciones: construye tu primer ETL"**. Aquí encontrarás ejemplos incrementales para aprender a usar Airflow desde lo más básico hasta DAGs más estructurados con buenas prácticas.

## 📁 Estructura del repositorio

dags/  
├── 1_estructura_basica.py # Primer DAG simple con dos tareas conectadas  
├── 2_xcoms.py # Introducción a la comunicación entre tareas usando XCom  
├── 3_agregar_params.py # Uso de params y cómo acceder a ellos desde las tareas  
├── 4_agregar_operadores.py # Ejemplo con operadores predefinidos (LambdaInvoke)  
├── 5_task_groups.py # Organización de tareas con Task Groups  
├── 6_callbacks.py # Uso de callbacks para manejar éxito y error de tareas  
├── 7_callback_fallido.py # Ejemplo de tarea fallida y cómo se dispara el callback  
└── params.py # Archivo auxiliar para definir parámetros reutilizables
Cada DAG está diseñado para enfocarse en un concepto específico de Airflow. Puedes ejecutarlos individualmente en tu entorno local de Airflow.

---

## ⚙️ Cómo correr estos DAGs

Asegúrate de tener un entorno de Airflow funcionando. 

### 📦 Instalación de Airflow

Para instalar Airflow en local, se recomienda hacerlo utilizando Docker, con el objetivo de facilitar la configuración del mismo.

Puedes encontrar una guía de instalación de Airflow utilizando Docker Compose en siguiente link:
- [Instalación de Airflow con Docker Compose](https://airflow.apache.org/docs/apache-airflow/2.10.5/howto/docker-compose/index.html)

> 💡 *Recomendamos usar Docker o WSL en Windows para evitar errores de compatibilidad.*

---

## 📚 Recursos de interés

- [Documentación oficial de Airflow](https://airflow.apache.org/docs/)
- [Guía sobre DAGs](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html)
- [Uso de XComs](https://airflow.apache.org/docs/apache-airflow/stable/concepts/xcoms.html)
- [Task Groups](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html#taskgroups)
- [Best practices para DAGs](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html)

---

