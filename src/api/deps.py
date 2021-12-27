from elasticsearch._async.client import AsyncElasticsearch
from starlette.requests import Request


def _get_es_connection(request: Request) -> AsyncElasticsearch:
    return request.app.state.es_client
