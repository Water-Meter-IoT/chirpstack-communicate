import paho.mqtt.client as mqtt
from google.cloud import pubsub_v1
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "credential/rd-iot-water-meter-18d3e6edd0c0.json"


def publish_message(data, application_id, dev_eui):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(
        'rd-iot-water-meter', f"lorawan-data")
    publisher.publish(topic_path, data=data.encode('utf-8'))
    print('Message published to Pub/Sub')


def on_connect(client, userdata, flags, rc):
    print('Connected to MQTT broker')
    client.subscribe('application/+/device/+/event/up')


def on_message(client, userdata, msg):
    topic_parts = msg.topic.split('/')
    application_id = topic_parts[1]
    dev_eui = topic_parts[3]
    print(f'Received MQTT message: {msg.payload.decode()}')
    publish_message(msg.payload.decode(), application_id, dev_eui)


broker_address = '34.101.68.124'
client_id = 'client-2'

client = mqtt.Client(client_id)
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address)
client.loop_forever()
