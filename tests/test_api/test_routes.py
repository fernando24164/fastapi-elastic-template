import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from starlette import status

pytestmark = pytest.mark.asyncio


@pytest.mark.skip('Integration test')
async def test_ingestion_endpoint(app: FastAPI, client: AsyncClient) -> None:
    event_data = {
        "title": "Test",
        "body": "does not matter",
        "description": "My cool event",
    }
    response = await client.post(app.url_path_for("ingestion:create"), json=event_data)
    assert response.status_code == status.HTTP_201_CREATED
