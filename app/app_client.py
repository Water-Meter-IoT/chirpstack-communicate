import base64
import tkinter as tk
from tkinter import ttk
import paho.mqtt.client as mqtt

# Konfigurasi MQTT broker ChirpStack
broker_address = '34.101.68.124'
port = 1883
# username = 'mqtt-username'
# password = 'mqtt-password'
client_id = 'client-4'
topic_template = 'application/2c31b8a7-c77d-4bd1-b9ff-d612198d0ccb/device/{dev_eui}/command/down'

# Fungsi untuk mengirim pesan ke broker MQTT
def send_mqtt_message(topic, payload):
    client = mqtt.Client(client_id)
    # client.username_pw_set(username, password)
    client.connect(broker_address, port)

    # Publish pesan ke topik MQTT
    client.publish(topic, payload)

    # Menutup koneksi MQTT
    client.disconnect()

# Fungsi untuk mengirimkan pesan ON ke relay
def send_relay_on():
    dev_eui = entry_dev_eui.get()
    topic = topic_template.format(dev_eui=dev_eui)

    message = "1"  # Mengirimkan data "1" untuk menyalakan relay
    payload = '{{"devEui": "{dev_eui}", "confirmed": true, "fPort": 1, "data": "{data}"}}'.format(dev_eui=dev_eui, data=base64.b64encode(message.encode()).decode())
    send_mqtt_message(topic, payload)

# Fungsi untuk mengirimkan pesan OFF ke relay
def send_relay_off():
    dev_eui = entry_dev_eui.get()
    topic = topic_template.format(dev_eui=dev_eui)

    message = "0"  # Mengirimkan data "0" untuk mematikan relay
    payload = '{{"devEui": "{dev_eui}", "confirmed": true, "fPort": 1, "data": "{data}"}}'.format(dev_eui=dev_eui, data=base64.b64encode(message.encode()).decode())
    send_mqtt_message(topic, payload)


# Membuat GUI dengan Tkinter
root = tk.Tk()
root.title("Device Control")

# Menggunakan tema ttk (themed tkinter) untuk tampilan yang lebih bagus
style = ttk.Style()
style.theme_use("clam")

# Frame utama
main_frame = ttk.Frame(root, padding=20)
main_frame.pack()

# Label dan Entry untuk DevEUI
dev_eui_frame = ttk.Frame(main_frame)
dev_eui_frame.pack(pady=10)

label_dev_eui = ttk.Label(dev_eui_frame, text="DevEUI:")
label_dev_eui.pack(side="left")
entry_dev_eui = ttk.Entry(dev_eui_frame)
entry_dev_eui.pack(side="left")
entry_dev_eui.insert(tk.END, "YOUR_DEV_EUI")  # Ganti dengan nilai default atau kosongkan jika ingin diisi oleh pengguna

# Tombol ON
btn_on = ttk.Button(main_frame, text="ON", width=10, command=send_relay_on)
btn_on.pack(pady=10)

# Tombol OFF
btn_off = ttk.Button(main_frame, text="OFF", width=10, command=send_relay_off)
btn_off.pack(pady=10)

# Menjalankan GUI
root.mainloop()
