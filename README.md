# Code MQTT to GCP Pub/Sub

Code ini adalah contoh implementasi pengiriman data dari broker MQTT ke Google Cloud Pub/Sub. Code ini menggunakan bahasa pemrograman Python.

## Deskripsi

Code ini membaca pesan-pesan yang dikirimkan ke broker MQTT dan meneruskannya ke topik di Google Cloud Pub/Sub. Pesan-pesan MQTT yang diterima akan difilter dan hanya data yang relevan akan dikirimkan ke Pub/Sub.

## Fitur

- Menerima pesan dari broker MQTT pada topik `application/+/device/+/event/up`.
- Memfilter pesan-pesan MQTT yang diterima sesuai dengan kriteria tertentu.
- Mengirimkan pesan-pesan yang telah difilter ke topik di Google Cloud Pub/Sub.

## Instalasi

1. Pastikan Anda memiliki Python 3.x dan pip terinstal di sistem Anda.
2. Clone repositori ini ke direktori lokal Anda.
3. Buka terminal dan navigasikan ke direktori Code.
4. Jalankan perintah berikut untuk menginstal dependensi yang diperlukan:
`pip install -r requirements.txt`

## Penggunaan

1. Pastikan Anda memiliki akses ke broker MQTT yang sesuai dengan konfigurasi yang diinginkan.
2. Ubah nilai variabel `broker_address` dan `client_id` pada kode sesuai dengan konfigurasi broker MQTT Anda.
3. Juga, pastikan Anda memiliki akses ke Google Cloud Platform (GCP) dan telah membuat Code dengan Cloud Pub/Sub di GCP.
4. Setelah itu, ubah nilai variabel `topic_path` pada kode sesuai dengan topik yang ingin Anda gunakan di Pub/Sub.
5. Jalankan kode dengan menjalankan perintah:
Windows :
`python publish_script.py`
Ubuntu :
`python3 publish_script.py`

6. Kode akan terhubung ke broker MQTT, menerima pesan-pesan yang masuk, melakukan filter, dan mengirimkan pesan-pesan yang difilter ke topik di Pub/Sub.

## Kontribusi

Kontribusi terhadap Code ini dipersilakan. Silakan buka "Issues" untuk melihat daftar tugas yang dapat dikerjakan atau tambahkan "Issue" baru jika Anda memiliki saran atau permintaan fitur.

## Lisensi

Code ini dilisensikan di bawah [MIT License](LICENSE).
