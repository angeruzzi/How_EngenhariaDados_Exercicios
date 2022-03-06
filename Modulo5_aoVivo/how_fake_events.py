#pip install boto3
#pip install fake_web_events

import boto3
import json
from fake_web_events import Simulation
from dotenv import load_dotenv
from os import getenv

load_dotenv('.env')
ACCESS_ID  = getenv('ACCESS_ID')
ACCESS_KEY = getenv('ACCESS_KEY')

client = boto3.client(
    'firehose', 
    region_name='us-east-1',
    aws_access_key_id=ACCESS_ID,
    aws_secret_access_key=ACCESS_KEY)

def put_record(event: dict):
    data = json.dumps(event) + "\n"
    response = client.put_record(
        DeliveryStreamName='egd-Alessandro',
        Record={"Data": data}
    )
    print(event)
    return response

simulation = Simulation(user_pool_size=100, sessions_per_day=100000)
events = simulation.run(duration_seconds=300)

for event in events:
    put_record(event)