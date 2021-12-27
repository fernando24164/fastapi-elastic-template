from fastapi import APIRouter
from src.api.v1.endpoints import ingestion

router = APIRouter()
router.include_router(ingestion.router, tags=["ingestion"], prefix="/v1")
