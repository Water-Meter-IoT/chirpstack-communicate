from google.cloud import pubsub_v1
from pymongo import MongoClient
import config
import json
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "credential/rd-iot-water-meter-94aabd3d232c.json"

project_id = "rd-iot-water-meter"
subscription_name = "lorawan-data-sub"
mongodb_uri = config.mongo_url
mongodb_database = "pubsub"
mongodb_collection = "chirpstack"

# Inisialisasi subscriber
subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(project_id, subscription_name)

# Inisialisasi MongoDB
mongo_client = MongoClient(mongodb_uri)
mongo_db = mongo_client[mongodb_database]
mongo_collection = mongo_db[mongodb_collection]


def process_data(data):
    parsed_data = json.loads(data)
    print("Parsed data:")
    for key, value in parsed_data.items():
        print(f"{key}: {value}")

    # Simpan data yang diuraikan ke MongoDB
    mongo_collection.insert_one(parsed_data)


def callback(message):
    data = message.data.decode('utf-8')
    print(f"Received message: {data}")

    # Proses data yang ada di dalam "data"
    process_data(data)

    message.ack()


# Mulai menerima pesan
streaming_pull_future = subscriber.subscribe(
    subscription_path, callback=callback)
print(f"Listening for messages on {subscription_path}...")

# Tambahkan Exception handling untuk menghentikan subscribe
try:
    streaming_pull_future.result()
except Exception as e:
    streaming_pull_future.cancel()
    print(f"Error occurred: {e}")
