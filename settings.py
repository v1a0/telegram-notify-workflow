from loguru import logger
from aiogram.types import ParseMode
import os

# Getting main environment variables
API_TOKEN = os.environ.get('secrets.TG_API_TOKEN')
CHAT_IDS = os.environ.get('secrets.TG_CHAT_IDS')

if not API_TOKEN:
    API_TOKEN = os.environ.get('secrets.WF_API_TOKEN')

if not CHAT_IDS:
    CHAT_IDS = os.environ.get('secrets.WF_CHAT_IDS')


# If main variables unset
if not API_TOKEN:
    raise EnvironmentError(f"Environment variable secrets.API_TOKEN unset or empty: {API_TOKEN=}")
if not CHAT_IDS:
    raise EnvironmentError(f"Environment variable secrets.CHAT_IDS unset or empty: {CHAT_IDS=}")


# Getting secondary environment variables
CHAT_IDS = CHAT_IDS.split()
REPO = os.environ.get('GITHUB_REPOSITORY')
ACTOR = os.environ.get('GITHUB_ACTOR')
EVENT = os.environ.get('GITHUB_EVENT_NAME')
REF = os.environ.get('GITHUB_REF')
HEAD_REF = os.environ.get('GITHUB_HEAD_REF')
BASE_REF = os.environ.get('GITHUB_BASE_REF')
SHA = os.environ.get('GITHUB_SHA')


# Logging results
print(f"{REPO=}")
print(f"{ACTOR=}")
print(f"{EVENT=}")
print(f"{REF=}")
print(f"{HEAD_REF=}")
print(f"{BASE_REF=}")
print(f"{SHA=}")


# Parser mode settings
PM = ParseMode.MARKDOWN


# Log settings
LOG_FILE_NAME = "_bot.log"
LOG_MODE = "DEBUG"
MAX_LOG_FILE_SIZE = "10Mb"
COMPRESSION = "zip"

LOG = logger.add(LOG_FILE_NAME, level=LOG_MODE, rotation=MAX_LOG_FILE_SIZE, compression=COMPRESSION)
