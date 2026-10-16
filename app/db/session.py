from sqlalchemy import create_engine

from app.core.config import get_settings
from sqlalchemy.orm import sessionmaker

settings = get_settings()
engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(bind=engine,autoflush=False)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()