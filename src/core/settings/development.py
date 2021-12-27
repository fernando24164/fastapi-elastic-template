import logging

from src.core.settings.app import AppSettings


class DevAppSettings(AppSettings):
    debug: bool = True

    title: str = "Dev FastAPI ingestion Elastic"

    logging_level: int = logging.DEBUG
