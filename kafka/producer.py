from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime
from config import KAFKA_BOOTSTRAP_SERVERS, TOPIC_NAME

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

users = [101, 102, 103, 104]
merchants = ["Amazon", "Flipkart", "Binance", "CryptoX"]
countries = ["IN", "SG", "AE", "US"]

while True:
    transaction = {
        "user_id": random.choice(users),
        "amount": random.randint(100, 120000),
        "merchant": random.choice(merchants),
        "country": random.choice(countries),
        "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    }

    producer.send(TOPIC_NAME, transaction)
    print("📤 Sent:", transaction)

    time.sleep(2)
