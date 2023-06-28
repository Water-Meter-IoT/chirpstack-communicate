import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud import pubsub_v1
import json
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "credential/rd-iot-water-meter-94aabd3d232c.json"

cred = credentials.Certificate(
    "credential/rd-iot-water-meter-firebase-adminsdk-n2q9z-2e5765b8be.json")
firebase_admin.initialize_app(cred)

project_id = "rd-iot-water-meter"
subscription_name = "chirpstack_integration-sub"
mongodb_database = "pubsub"
mongodb_collection = "chirpstack"

db = firestore.client()

# Inisialisasi subscriber
subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(project_id, subscription_name)



def process_data(data):
    parsed_data = json.loads(data)
    # print("Parsed data:")
    # for key, value in parsed_data.items():
    #     print(f"{key}: {value}")

    dev_eui = parsed_data.get("deviceInfo", {}).get("devEui")  # Mengambil nilai devEui dari parsed_data
    if dev_eui:
        # Filter data yang diperlukan
        filtered_data = {
            "time": parsed_data.get("time"),
            "deviceInfo": {
                "applicationId": parsed_data.get("deviceInfo", {}).get("applicationId"),
                "devEui": dev_eui
            },
            "data": parsed_data.get("data"),
            "object": parsed_data.get("object")
        }

        print("Filtered data:")
        for key, value in filtered_data.items():
            print(f"{key}: {value}")

        # Simpan data yang diuraikan ke Firestore
        doc_ref = db.collection("chirpstack").document(dev_eui)
        doc_ref.set(filtered_data)
        print(f"Data saved to Firestore document '{dev_eui}'")
    else:
        print("devEui not found in parsed data")


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
