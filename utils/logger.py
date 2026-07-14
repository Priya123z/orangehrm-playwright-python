from loguru import logger
import os

os.makedirs("logs", exist_ok=True)

logger.remove()

logger.add(
    "logs/framework.log",
    rotation="10 MB",
    retention="10 days",
    level="INFO",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}"
)