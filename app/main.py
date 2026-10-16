import logging

from fastapi import FastAPI
from app.core.logging import setup_logging
from app.db.session import get_db
from sqlalchemy.orm import Session
from fastapi import Depends

setup_logging()

logger = logging.getLogger(__name__)

app = FastAPI()

logger.info("TaskForge started")
@app.get("/test-db")
def test_db(db: Session = Depends(get_db)):
    return {"session_created": True}

@app.get("/test-error")
def test_error():
    logger.error("This is a test error")
    return {"logged": True}

@app.get("/health")
async def health():
    return {"status": "ok"}