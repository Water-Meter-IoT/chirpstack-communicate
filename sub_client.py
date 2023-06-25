from google.cloud import pubsub_v1
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "credential/rd-iot-water-meter-94aabd3d232c.json"

project_id = "rd-iot-water-meter"
subscription_name = "lorawan-data-sub"

# Inisialisasi subscriber
subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(project_id, subscription_name)


def callback(message):
    print(f"Received message: {message.data.decode('utf-8')}")
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
