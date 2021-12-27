from elasticsearch._async.client import AsyncElasticsearch
from fastapi import FastAPI
from loguru import logger


async def connect_to_db(app: FastAPI) -> None:
    logger.info("Connecting to ElasticSearch")

    app.state.es_client = AsyncElasticsearch(
        ["http://elastic:changeme@localhost:9200/"]
    )

    logger.info("Connection established")


async def close_db_connection(app: FastAPI) -> None:
    logger.info("Closing connection to ElasticSearch")

    await app.state.es_client.close()

    logger.info("Connection closed")
