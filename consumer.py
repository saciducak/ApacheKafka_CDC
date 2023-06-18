from kafka import KafkaConsumer

# Kafka yapılandırması
bootstrap_servers = ['localhost:9092']
topic = 'X'

# Kafka Consumer oluşturma
consumer = KafkaConsumer(topic, bootstrap_servers=bootstrap_servers)

# Mesajları tüketme
for message in consumer:
    print(message.value.decode('utf-8'))
