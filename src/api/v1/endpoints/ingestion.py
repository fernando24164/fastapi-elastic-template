from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from starlette import status
from src.api.deps import _get_es_connection
from src.services.elastic import elastic_ingestion
from src.models.schemas.logger_events import LoggerEvent

router = APIRouter()


@router.post(
    "/ingestion_events",
    status_code=status.HTTP_201_CREATED,
    name="ingestion:create",
)
async def create_log_events(
    event: LoggerEvent, es_connection=Depends(_get_es_connection)
) -> JSONResponse:
    """
    Create new item.
    """
    await elastic_ingestion(es_connection, event)
    return JSONResponse(status_code=201)
