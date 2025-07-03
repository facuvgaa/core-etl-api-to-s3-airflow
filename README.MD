# 🌐 core-etl-api-to-s3-airflow

Este proyecto automatiza un pipeline de datos que extrae información desde una API pública, la guarda en una base de datos SQLite, luego la transforma a CSV usando `pandas`, y finalmente la sube a AWS S3.

> 🧰 Usa una biblioteca propia en Python: [`core-extract-and-load`](https://pypi.org/project/core-extract-and-load/) para las operaciones de extracción y guardado.

> ⚙️ Todo el proceso está orquestado mediante un DAG de Apache Airflow y ejecutado en contenedores Docker.

---

## 📚 Tabla de contenido

- [📘 Sobre el proyecto](#📘-sobre-el-proyecto)
- [🛠 Tecnologías](#🛠-tecnologías)
- [📦 Instalación](#📦-instalación)
- [🔐 Variables de entorno](#🔐-variables-de-entorno)
- [🚀 Uso](#🚀-uso)
- [🗂 Estructura del proyecto](#🗂-estructura-del-proyecto)
- [🔁 Pipeline de datos](#🔁-pipeline-de-datos)
- [🧪 Ejemplo de ejecución](#🧪-ejemplo-de-ejecución)
- [📝 Licencia](#📝-licencia)
- [✍️ Autor](#✍️-autor)
- [📎 Recursos](#📎-recursos)

---

## 📘 Sobre el proyecto

Este proyecto fue desarrollado como parte de una prueba técnica para demostrar habilidades en:

- Automatización de pipelines ETL
- Desarrollo de bibliotecas propias en Python
- Transformación de datos con `pandas`
- Almacenamiento en AWS S3
- Orquestación con Apache Airflow

---

## 🛠 Tecnologías

- Python 3.12
- Apache Airflow 3.0.2
- Docker / Docker Compose
- SQLite
- pandas
- Amazon S3
- [`core-extract-and-load`](https://pypi.org/project/core-extract-and-load/)

---

## 📦 Instalación

```bash
# Clonar el repositorio
git clone https://github.com/facuvgaa/core-etl-api-to-s3-airflow.git
cd core-etl-api-to-s3-airflow

# Crear archivo de variables de entorno
cp .env.example .env
# Editar el archivo .env con tus credenciales de AWS

# Levantar Airflow con Docker
docker-compose up -d
```

---

## 🔐-variables-de-entorno

 # crear un punto .env con las siguientes credenciales 

```bash
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_BUCKET_NAME=your_bucket_name
DB_PATH=/tmp/demo.db
S3_FILENAME=output.csv
```
---
## 🚀-uso

para ejecutar el dag hay que ingresar al aiflow levantado que se ejecuta en 

 http://192.168.100.33:8080/
 
 para el admin y password de logueo es necesario ingresar a la instancia de airflow con el siguiente comando 

 sudo docker exec -it airflow bash 
 cat simple_auth_manager_passwords.json.generated

 se muestran las credenciales de logueo ejemplo {"admin": "gteQPKHS5TPFc9mH"}

 ejecutar el Dag

---

 ## 🔁 Pipeline de datos

El pipeline está desarrollado en Apache Airflow y sigue el patrón ETL (Extract, Transform, Load). Se compone de las siguientes etapas:

1. **Extracción (Extract):**
   - Se realiza una consulta a una API pública (https://api.bluelytics.com.ar/v2/latest).
   - Los datos obtenidos son formatos como JSON o similares.

2. **Transformación (Transform):**
   - Se realiza una limpieza y transformación y se guarda en una base de datos sqlite.db.


3. **Carga (Load):**
   - se extrar de la base de datos con pandas los ultimos datos agregados, se los limpia .
   - se descarga el archivo csv que esta en S3 se agrega los ultimos datos y se vuelve a subir el archivo modificado.

Este proceso está automatizado mediante un DAG de Airflow que se ejecuta según una programación definida y puede monitorearse desde la interfaz web de Airflow.

---

## 🧪 Ejemplo de ejecución

Una vez desplegado el DAG en Airflow, se puede ejecutar manualmente o esperar la ejecución automática según la programación definida.

### Resultado esperado:

- Airflow descarga datos desde la API.
- Transforma los datos y los guarda en formato `.sqlite`.
- con pandas transforma los datos en la DB y los pasa a csv y luego descarga el archivo csv de s3 y agrega el ultimo dato.
- sube el archivo csv con los datos ya agregados:

```bash
Log message source details: sources=["/opt/airflow/logs/dag_id=dag_extractar_guardar_y_subir/run_id=scheduled__2025-07-02T03:00:00+00:00/task_id=tarea_save/attempt=1.log"]
[2025-07-02, 17:43:16] INFO - DAG bundles loaded: dags-folder: source="airflow.dag_processing.bundles.manager.DagBundlesManager"
[2025-07-02, 17:43:16] INFO - Filling up the DagBag from /opt/airflow/dags/dag.py: source="airflow.models.dagbag.DagBag"
[2025-07-02, 17:43:16] INFO - MainDTO(aws_access_key_id='AKIA6G75DVRKJUMP6SPG', aws_secret_access_key='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', bucket_name='guardado-dolar', region_name='us-east-1', s3_filename='archivo.csv', db_path='/tmp/airflow.db'): chan="stdout": source="task"
[2025-07-02, 17:43:16] INFO - us-east-1: chan="stdout": source="task"
[2025-07-02, 17:43:17] INFO - <botocore.client.S3 object at 0x73624abca7e0> guardado-dolar archivo.csv /tmp/archivo.csv: chan="stdout": source="task"
[2025-07-02, 17:43:17] INFO - Descargado: s3://guardado-dolar/archivo.csv: chan="stdout": source="task"
[2025-07-02, 17:43:17] INFO - Subido a s3://guardado-dolar/archivo.csv: chan="stdout": source="task"
[2025-07-02, 17:43:17] INFO - Done. Returned value was: None: source="airflow.task.operators.airflow.providers.standard.decorators.python._PythonDecoratedOperator"
```
---

## 📝 Licencia

Este proyecto está licenciado bajo la [Licencia MIT](LICENSE).

---

## ✍️ Autor

Desarrollado por **Facundo Vega**  
📧 Email: facundovega.dev@gmail.com  
💼 GitHub: [facuvgaa](https://github.com/facuvgaa)

🧠 Si te sirvió este proyecto, no olvides dejar una estrella ⭐ en el repositorio.

---

##📎-recursos

- Documentación oficial de [Apache Airflow](https://airflow.apache.org/docs/)
- Guía de instalación de [Docker](https://docs.docker.com/get-docker/)
- core-extract-and-load  [core-extract-to-load ](https://pypi.org/project/core-extract-and-load/) 
- SDK de [Amazon S3 (boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- pandas sql to csv [pandas to csv](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html/)

---


