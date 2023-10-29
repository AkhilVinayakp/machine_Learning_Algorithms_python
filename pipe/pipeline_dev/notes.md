

# Airflow
- setup: local : Ubuntu WSL2
- commands
    `airflow scheduler`
    ` airflow webserver --port 8050  `

# Jenkins
- setup: local : Docker : image => Jenkins:blueocean
- port: 8080

# MLflow
- setup: local : Windows 11
- Port: 5000
- commands
    ` mlflow ui  `

# Prefect
    `prefect server start`
    http://127.0.0.1:4200/dashboard  port
    


# ELK stack for logging




# How to automate

ansible playbooks ?


# Data Pipelines
> Project: DataPipeline <br/>
implementation file: datapipe_pre.py
Running the file directly will run inside prefect

Add a deployment to prefect: `python pipeconf.py serve <Name>`




# DVC
sample commands
dvc add .\data\wine.csv  to add to dvc

- new files created - wine.csv.dvc
git add wine.csv.dvc
git commit -m 'dv1.0'



