import paho.mqtt.client as mqtt
import json

broker_address = '34.101.68.124'
port = 1883
client_id = 'client-1'


def send_mqtt_message(topic, payload):
    client = mqtt.Client(client_id)
    client.connect(broker_address, port)

    # Publish pesan ke topik MQTT
    client.publish(topic, payload)

    # Menutup koneksi MQTT
    client.disconnect()


# Konfigurasi downlink
application_id = '2c31b8a7-c77d-4bd1-b9ff-d612198d0ccb'
dev_eui = '06634f93b876a32b'
f_port = 1
payload_data = 'SGVsbG8gTG9yYQ=='  # Contoh: 'Hello Lora' dalam base64 encoded
object_data = {
    "temperatureSensor": {"1": 25},
    "humiditySensor": {"1": 32}
}
confirmed = True

# Membuat payload dalam format JSON
payload = {
    "devEui": dev_eui,
    "confirmed": confirmed,
    "fPort": f_port,
    "data": payload_data,
    "object": object_data
}

# Mengirimkan pesan ke ChirpStack
topic = f'application/{application_id}/device/{dev_eui}/command/down'
send_mqtt_message(topic, json.dumps(payload))
