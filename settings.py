from loguru import logger
from aiogram.types import ParseMode
import os

API_TOKEN = os.environ.get('secrets.WF_API_TOKEN')
CHAT_IDS = os.environ.get('secrets.WF_CHAT_IDS').split()

if not API_TOKEN:
    os.environ.get('secrets.TG_API_TOKEN')

if not CHAT_IDS:
    os.environ.get('secrets.TG_CHAT_IDS').split()


REPO = os.environ.get('GITHUB_REPOSITORY')
ACTOR = os.environ.get('GITHUB_ACTOR')
EVENT = os.environ.get('GITHUB_EVENT_NAME')
REF = os.environ.get('GITHUB_REF')


PM = ParseMode.MARKDOWN

LOG_FILE_NAME = "_bot.log"
LOG_MODE = "DEBUG"
MAX_LOG_FILE_SIZE = "10Mb"
COMPRESSION = "zip"

LOG = logger.add(LOG_FILE_NAME, level=LOG_MODE, rotation=MAX_LOG_FILE_SIZE, compression=COMPRESSION)
