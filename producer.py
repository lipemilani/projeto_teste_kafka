import json
from time import sleep
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9091'],
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                         api_version=(2,6,0))
                         
##################################################################
data = {
    'id': 1,
    'msg': 'msg numero 1',
}
producer.send('cookie', value=data)
print('msg 1 enviada')
sleep(1)
##################################################################
data = {
    'id': 2,
    'msg': 'msg numero 2',
}
producer.send('cookie', value=data)
print('msg 2 enviada')
sleep(1)
##################################################################
data = {
    'id': 3,
    'msg': 'msg numero 3',
}
producer.send('cookie', value=data)
print('msg 3 enviada')
sleep(1)
##################################################################
data = {
    'id': 4,
    'msg': 'msg numero 4',
}
producer.send('cookie', value=data)
print('msg 4 enviada')
sleep(1)