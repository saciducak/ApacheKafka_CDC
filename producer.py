from pymongo import MongoClient
from kafka import KafkaProducer
from json import dumps

# MongoDB bağlantısı
client = MongoClient('mongodb://localhost:27017')
db = client['mydatabase']
collection = db['mycollection']

# Kafka yapılandırması
bootstrap_servers = ['localhost:9092']
topic = 'X'

# Kafka Producer oluşturma
producer = KafkaProducer(bootstrap_servers=bootstrap_servers, value_serializer=lambda x: dumps(x).encode('utf-8'))

# Değişiklikleri izleme
pipeline = [{'$match': {'operationType': 'insert'}}]
with collection.watch(pipeline) as stream:
    for change in stream:
        document = change['fullDocument']
        producer.send(topic, value=document)
        producer.flush()
