from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from airflow import DAG
from datetime import datetime
from airflow.utils.dates import days_ago

args = {
    "owner": "stopleaf",
    "email_on_failure": False,
}
dag = DAG(
    dag_id="seoulrtd_citydata_kafka_pub",
    start_date=days_ago(1),
    schedule_interval="*/1 * * * *",
    max_active_runs=1,
    default_args=args,
    catchup=False
)

start = EmptyOperator(task_id="start", dag=dag)
end = EmptyOperator(task_id="end", dag=dag)

t1 = BashOperator(
    task_id="collect_data",
    bash_command="/Users/stopleaf/.pyenv/versions/seoul/bin/python /Users/stopleaf/PycharmProjects/seoulrtd_citydata/kafka_producer.py",
    retries=1,
    dag=dag,
)

start >> t1 >> end