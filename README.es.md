# Fastapi-elastic-template WIP

[![es](https://img.shields.io/badge/lang-en-green.svg)](./README.md)

## Contenido

- [Información](#about)
- [Instalación](#getting_started)

## Información <a name = "about"></a>

Proyecto de ejemplo de ingestión con ElasticSearch y FastAPI

## Instalación <a name = "getting_started"></a>

### Prerequitos

Instalar docker-compose

[Install docker compose](https://docs.docker.com/compose/install/)

### Despliegue en local

Para lanzar ElasticSearch

```
docker-compose up
```

Si docker-compose falla quizá necesite ejecutar

```
sudo sysctl -w vm.max_map_count=262144
```

Conéctese a `localhost:9200` puede que solicite nombre y contraseña:

```
ELASTICSEARCH_USERNAME=elastic
ELASTIC_PASSWORD=changeme
```

Para crear un indice en ElasticSearch llamado `ingestion_index`

```
curl --request PUT \
  --url 'http://localhost:9200/userindex2?pretty=' \
  --header 'Content-Type: application/json' \
  --data '{
  "settings": {
    "index": {
      "number_of_shards": 1,
      "number_of_replicas": 0
    }
  }
}'
```

### Como desplegar la interfaz de python?

Para lanzar la aplicación de python

```
uvicorn src.main:app
```

El servidor estara escuchando en http://127.0.0.1:8000
En este dirección se puede acceder al la URL que nos permite añadir eventos en ElasticSearch.