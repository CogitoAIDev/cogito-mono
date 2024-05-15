import logging
import os
from dotenv import load_dotenv

from .constants import LEVEL_LOGGING


logger = logging.getLogger('cogito_logger')
logger.setLevel(LEVEL_LOGGING)

file_handler = logging.FileHandler('cogito.log')
file_handler.setLevel(LEVEL_LOGGING)

console_handler = logging.StreamHandler()
console_handler.setLevel(LEVEL_LOGGING)

formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)
