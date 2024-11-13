## Clone repo ini
```shell
git clone -b fsub https://github.com/Syuhadak27/python-cari-link.git && cd python-cari-link
```

Deskripsi

## Perintah Docker

Untuk menjalankan Docker daemon, gunakan perintah berikut:

```shell
sudo dockerd
```
Untuk membuat image docker
```shell
sudo docker build . -t syd
```
Untuk menjalankan image docker
```shell
sudo docker run -p 80:80 -p 8080:8080 syd
```
## Perintah Build tanpa Port
```shell
sudo docker build -t syd .
```
```shell
sudo docker run -d --restart unless-stopped syd
```
## Perintah Lainnya

Berikut beberapa perintah lain yang mungkin berguna:

Untuk melihat docker image yang berjalan
```shell
sudo docker ps
```
untuk menghentikan image docker yg berjalan
```shell
sudo docker stop ID_DARI_Docker
```
