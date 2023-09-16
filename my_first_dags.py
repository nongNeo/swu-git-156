from __future__ import annotations

# [START tutorial]
# [START import_module]
from datetime import datetime, timedelta
from textwrap import dedent

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator

with DAG(
    "my_first_dags1",
    default_args={
        "email": ["nattapat.musitmanee@g.swu.ac.th"],
    },
    description="A simple tutorial DAG",
    schedule=None,
    start_date=datetime(2021, 1, 1),
    tags=["example"],
) as dag:
	from airflow import DAG
	from airflow.operators.python_operator import BranchPythonOperator
	from airflow.operators.dummy_operator import DummyOperator 
	from datetime import datetime

	def separate_even_and_odd(numbers):
		even_numbers = []
		odd_numbers = []
   
		for num in numbers:
			if num % 2 == 0:
				even_numbers.append(num)
			else:
				odd_numbers.append(num)
    	
		return even_numbers, odd_numbers
	A_task = DummyOperator(task_id='branch_a', dag=dag)
	B_task = DummyOperator(task_id='branch_false', dag=dag)

	branch_task = BranchPythonOperator(
		task_id='branching',
		python_callable=separate_even_and_odd,
		dag=dag,
		)
	branch_task >> A_task
	branch_task >> B_task
