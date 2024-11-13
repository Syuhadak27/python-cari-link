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


## Deploy ke HEROKU

```shell
heroku git:remote -a nama app
```

```shell
git add . 
```

 ```shell
git commit -am "make it better" 
```
```shell
git push heroku main
```
```shell
heroku logs -t
```

(Optional)
Disable DYNO
$ heroku ps:scale worker=0
ENABLE DYNO
$ heroku ps:scale worker=1

Jika gagal 
heroku git:remote -a 
git rm -r *
git commit -m "Remove all files"
git push heroku main --force

Deploy Ulang

git add .

git commit -m "Re-deploying all files"

git push heroku main --force
