from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'airscholar',
    'start_date': datetime(2025, 7, 27),
}


def get_data():
    import json
    import requests

    res = requests.get("https://randomuser.me/api/")
    res = res.json()
    res = res['results'][0]
   
    return res



def format_data(res):
    
    data = {}
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    data['email'] = res['email']
    data['phone'] = res['phone']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']['date']
    data['registered_date'] = res['registered']['date']
    data['postcode'] = res['location']['postcode']
    data['picture'] = res['picture']['medium']
    return data
    
def stream_data():
    import json
    res = get_data()
    data = format_data(res)
    print(json.dumps(data, indent=3))


# with DAG( 'user_automation',
#     default_args = default_args,
#     schedule_interval = '@daily',
#     catchup = False) as dag:
    
#     streaming_task = PythonOperator(
#         task_id='stream_data_from_api',
#         python_callable= stream_data,      
     
# )

stream_data()