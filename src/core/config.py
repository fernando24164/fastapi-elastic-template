from functools import lru_cache
from typing import Dict, Type

from src.core.settings.app import AppSettings
from src.core.settings.base import AppEnvTypes
from src.core.settings.development import DevAppSettings
from src.core.settings.test import TestAppSettings

environments: Dict[AppEnvTypes, Type[AppSettings]] = {
    "dev": DevAppSettings,
    "test": TestAppSettings,
}


@lru_cache
def get_app_settings() -> AppSettings:
    app_env = "dev"
    config = environments[app_env]
    return config(app_env=app_env)
