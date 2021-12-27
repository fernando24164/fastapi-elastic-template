from uuid import uuid4

from elasticsearch import AsyncElasticsearch
from src.models.schemas.logger_events import LoggerEvent

INDEX = "log_events"


async def elastic_ingestion(es_client: AsyncElasticsearch, event: LoggerEvent) -> bool:
    response = await es_client.create(index=INDEX, document=event.dict(), id=str(uuid4()))
    return bool(response)
