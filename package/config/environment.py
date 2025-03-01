"""
Store all package's environment variables.
"""

from os import environ

from dotenv import load_dotenv

load_dotenv()

USER_NAME=environ.get("USER_NAME")
