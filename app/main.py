import logging

from fastapi import FastAPI
from app.core.logging import setup_logging

setup_logging()

logger = logging.getLogger(__name__)

app = FastAPI()

logger.info("TaskForge started")


@app.get("/test-error")
def test_error():
    logger.error("This is a test error")
    return {"logged": True}

@app.get("/health")
async def health():
    return {"status": "ok"}