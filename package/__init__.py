"""
Direct imports for the package library.
"""

from package.config.environment import USER_NAME, DATA_DIRECTORY


def hello_world(name: str) -> str:
    print(DATA_DIRECTORY)
    print(f"Hello {USER_NAME}")

    return name
