from datetime import timedelta
import pendulum
from airflow.decorators import dag, task
from core_extract_and_load import extract_and_load, actualizar_csv_s3_con_sqlite, MainDTO
import os

@dag(
    dag_id="dag_extractar_guardar_y_subir",
    schedule="@daily",
    start_date=pendulum.datetime(2025, 6, 24, tz="America/Argentina/Tucuman"),
    catchup=False,
    default_args={"retries": 1, "retry_delay": timedelta(minutes=5)},
    tags=["etl"]
)
def dag_extact_and_save():
    
    @task()
    def tarea_and_load():
        db_path = os.getenv("DB_PATH")
        extract_and_load(db_path)

    @task()
    def tarea_save():
        dto = MainDTO(
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        bucket_name=os.getenv("AWS_BUCKET_NAME"),
        region_name=os.getenv("AWS_REGION"),
        s3_filename=os.getenv("S3_FILENAME"),
        db_path=os.getenv("DB_PATH")
    )
        actualizar_csv_s3_con_sqlite(dto)

    tarea_and_load() >> tarea_save()

dag = dag_extact_and_save()