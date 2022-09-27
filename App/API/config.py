from pydantic import BaseSettings, AnyHttpUrl
from typing import List, cast
from types import FrameType

import logging
from loguru import logger
import sys


class LoggingSettings(BaseSettings):
    LOGGING_LEVEL: int = logging.INFO


class Settings(BaseSettings):
    API_V1_STR: str = "/api"
    PROJECT_NAME: str = "Titanic survival"
    
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost:3000",
        "http://localhost:8000",
        "https://localhost:3000",
        "https://localhost:8000",]
    
    logging: LoggingSettings = LoggingSettings()
    
    
class InterceptHandler(logging.Handler):
    
    def emit(self, record: logging.LogRecord) -> None:
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = str(record.levelno)
            
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = cast(FrameType, frame.f_back)
            depth = depth+1
            
        logger.opt(depth = depth, exception = record.exc_info).log(level, record.getMessage())
    
    
def setup_app_logging(config: Settings) -> None:
    
    LOGGERS = ("uvicorn.asgi", "uvicorn.access")
    logging.getLogger().handlers = [InterceptHandler()]
    
    for logger_name in LOGGERS:
        logging_logger = logging.getLogger(logger_name)
        logging_logger.handlers = [InterceptHandler(level = config.logging.LOGGING_LEVEL)]
        
    logger.configure(
        handlers = [{"sink": sys.stderr, "level": config.logging.LOGGING_LEVEL}])


settings = Settings()