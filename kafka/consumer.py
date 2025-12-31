from kafka import KafkaConsumer
import json
from config import KAFKA_BOOTSTRAP_SERVERS, TOPIC_NAME, GROUP_ID
from api.predict import predict_and_store

consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    group_id=GROUP_ID,
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    auto_offset_reset="latest",
    enable_auto_commit=True
)

print("🚀 Kafka Consumer Started...")

for message in consumer:
    transaction = message.value
    print("📥 Received:", transaction)

    result = predict_and_store(transaction)
    print("✅ Stored:", result)
