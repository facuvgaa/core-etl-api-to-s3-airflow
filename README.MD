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
- Apache Airflow
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