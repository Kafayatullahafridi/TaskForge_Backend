import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path

from app.core.config import get_settings


def setup_logging() -> None:
    settings = get_settings()

    # ─── Prepare log directory ────────────────────────
    log_file = Path(settings.LOG_FILE_PATH)
    log_file.parent.mkdir(parents=True, exist_ok=True)

    # ─── Shared formatter ─────────────────────────────
    formatter = logging.Formatter(settings.LOG_FORMAT)

    # ─── Root logger ──────────────────────────────────
    logger = logging.getLogger()
    logger.setLevel(settings.LOG_LEVEL.upper())

    # Avoid duplicate handlers if setup_logging() runs twice
    # (e.g. uvicorn --reload, tests, notebooks)
    if logger.hasHandlers():
        logger.handlers.clear()

    # ─── Console handler (everything at LOG_LEVEL) ────
    if settings.LOG_TO_CONSOLE:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(settings.LOG_LEVEL.upper())
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    # ─── File handler (everything at LOG_LEVEL) ───────
    if settings.LOG_TO_FILE:
        file_handler = RotatingFileHandler(
            filename=settings.LOG_FILE_PATH,
            maxBytes=settings.LOG_FILE_MAX_BYTES,
            backupCount=settings.LOG_FILE_BACKUP_COUNT,
            encoding="utf-8",
        )
        file_handler.setLevel(settings.LOG_LEVEL.upper())
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    # ─── Error-only file handler (ERROR and above) ────
    error_handler = RotatingFileHandler(
        filename=log_file.parent / "errors.log",
        maxBytes=settings.LOG_FILE_MAX_BYTES,
        backupCount=settings.LOG_FILE_BACKUP_COUNT,
        encoding="utf-8",
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)
    logger.addHandler(error_handler)

    # ─── Optional: silence noisy third-party loggers ──
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)