from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
    'cookie',
     bootstrap_servers=['localhost:9091'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')),
     api_version=(2,6,0))

for message in consumer:
    message = message.value
    print(message)