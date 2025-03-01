<h1 align="center">DATASCIENCE PROJECT TEMPLATE</h1>

_<h4 align="center">A starter template for datascience projects (by [Anatole-DC](https://github.com/Anatole-DC))</h4>_

This project describes what could be considered a good starting architecture for datascience projects. This project aims at providing a clean directory organization to anticipate future refactoring headaches.

Most important points of this template :
- Using [pyproject.toml](pyproject.toml) instead of requirements.txt
- Splitting package into smaller modules (see [project's documentation](/documentation/README.md))
- Training [models into sub apps](/apps/models/README.md)
- [Custom package cli](/package/cli/README.md) for easier workflow
- Extensive [.gitignore](.gitignore)
- Code quality tools (see [here](/documentation/best_practices.md#code-quality) on how to use them)
- [Makefile](Makefile) with commands shortcuts

## Summary

- [Summary](#summary)
- [Getting Started](#getting-started)
  - [Requirements](#requirements)
  - [Setup](#setup)
  - [Working on the project](#working-on-the-project)
- [Project structure](#project-structure)
- [Getting further](#getting-further)
- [Raising issues](#raising-issues)

## Getting Started

The following section describes how to get started with this template.

### Requirements

**Pyenv (Required)**

```bash
pyenv --version
# pyenv 2.5.0
```

**Make (Optionnal)**

```bash
make --version
# GNU Make 4.3
# Built for x86_64-pc-linux-gnu
# Copyright (C) 1988-2020 Free Software Foundation, Inc.
# License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
# This is free software: you are free to change and redistribute it.
# There is NO WARRANTY, to the extent permitted by law.
```

**Git (Optionnal)**

```bash
git --version
git version 2.34.1
```

### Setup

Configure python.

```bash
make pyenv-setup
make env-setup
```

Install the dependencies.

```bash
# Run this command when you update the pyproject.toml
make install

# Install the dev and test dependencies
make dev-install
make test-install
```

### Working on the project

See [this document on coding best practices](/documentation/best_practices.md) and [this document on git and github workflow](/documentation/git_github_workflow.md) to start developping.

**Generate new model**

```bash
make new-model MODEL_NAME="model_name"
```

> This will generate a new model inside the [models](/apps/models/) directory, with a `main.py` and a `README.md`.  
> The `main.py` is generated from [this template file](/assets/templates/model_template.py) so update it for more complete starter models.

## Project structure

```bash
ds_project_template/
├── apps
│   ├── models
│   │   ├── model_1
│   │   │   ├── cache
│   │   │   └── main.py
│   │   └── README.md
│   └── website
│       └── README.md
├── data
│   └── README.md
├── documentation
├── makefile
├── package
│   ├── cli
│   │   ├── cli_main.py
│   │   └── README.md
│   ├── config
│   │   ├── environment.py
│   │   ├── logger.py
│   │   └── README.md
│   ├── data
│   │   ├── database.py
│   │   ├── loader.py
│   │   ├── preprocessing.py
│   │   └── README.md
│   ├── __init__.py
│   ├── measures
│   │   └── README.md
│   └── models
│       └── README.md
├── pyproject.toml
├── README.md
├── requirements.txt
└── scripts
    └── README.md
```

## Getting further

If you are interested in a more complete set of tools, see [this repository](https://github.com/Anatole-DC/template_python).

## Raising issues

If you find issues or misleading informations, feel free to raise an issue.
