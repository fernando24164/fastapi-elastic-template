# Fastapi-elastic-template WIP

[![es](https://img.shields.io/badge/lang-es-green.svg)](./README.es.md)

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)

## About <a name = "about"></a>

Example project to ingest events in ElasticSearch with FastAPI endpoint

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

Install docker-compose

[Install docker compose](https://docs.docker.com/compose/install/)

### Installing

To launch the elasticsearch

```
docker-compose up
```

if docker-compose fail maybe you need to execute

```
sudo sysctl -w vm.max_map_count=262144
```

Connect to `localhost:9200` it will request username and password

```
ELASTICSEARCH_USERNAME=elastic
ELASTIC_PASSWORD=changeme
```

To create an Elastic index called ingestion_index

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

Install python dependencies

```
pip install -r requirements.txt
```

# How to launch

To launch the python API

```
uvicorn src.main:app
```

Server will run on http://127.0.0.1:8000. There you can access
to the endpoint via Swagger interface and test it on your local.