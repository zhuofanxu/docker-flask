Flask gunicorn nginx postgresql redis development env with docker
=================================================

## Reference resources:
* [docker-official-docs](https://github.com/docker-library/docs)
* [www.ameyalokare.com](http://www.ameyalokare.com/docker/2017/09/20/nginx-flask-postgres-docker-compose.html)
* [yeasy Docker —— 从入门到实践](https://legacy.gitbook.com/book/yeasy/docker_practice/details)


## Requirements
docker server version: 18.06.1-ce and newer

docker-compose version 1.22.0, build f46880f and newer

## Usage
Create and start containers
```shell
cd docker-flask && docker-compose up
```
access server via nginx
```shell
curl http://localhost:8000
```
access server via gunicorn directly
```shell
curl http://localhost:8080
```