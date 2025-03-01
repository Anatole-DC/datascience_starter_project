"""
Direct imports for the package library.
"""

from package.config.environment import USER_NAME


def hello_world():
    print(f"Hello {USER_NAME}")
