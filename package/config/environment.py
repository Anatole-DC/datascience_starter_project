"""
Store all package's environment variables.
"""

from os import environ
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

PROJECT_DIRECTORY = Path(environ.get("PROJECT_DIRECTORY"))

CACHE_DIRECTORY = PROJECT_DIRECTORY / "cache"

DATA_DIRECTORY = Path(environ.get("DATA_DIR", PROJECT_DIRECTORY / "data"))
DATA_DIRECTORY.mkdir(exist_ok=True, parents=True)

USER_NAME = environ.get("USER_NAME")
