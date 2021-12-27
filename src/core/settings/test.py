import logging
from uuid import uuid4

from pydantic import SecretStr

from src.core.settings.app import AppSettings


class TestAppSettings(AppSettings):
    debug: bool = True

    title: str = "Test FastAPI ingestion Elastic"

    logging_level: int = logging.DEBUG
