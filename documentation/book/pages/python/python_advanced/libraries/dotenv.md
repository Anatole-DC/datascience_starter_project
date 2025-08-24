# Dotenv

Dotenv is a library that reads and loads environment variables from a `.env` file.

## Why this instead of `direnv`

- Because is a standardized way of doing things between multiple languages.
- Because it's a painpoint when developpers have to install another tool.

## How to use it

Installation :

```bash
pip install python-dotenv
```

Import and usage :

```python
from os import environ
from dotenv import load_environ

load_environ()

MY_ENV_VAR = environ.get("ENV_VAR_NAME_IN_DOTENV")
```

```{admonition} Tip !
Create a `config.py` or `environment.py` in your project, and load and create all your environment and project variables within this file.

This allows you to only make one `load_environ` function call, as well as making all your variables accessible from one place.
```
