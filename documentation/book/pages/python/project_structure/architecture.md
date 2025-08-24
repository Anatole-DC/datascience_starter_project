# Project architecture

This section presents every directory and its role inside the project.

## Package

Contain your library source code that will be used within the apps.

## Apps

Contains all the executable and interfaces that will use your package's code.

```{note}
We will talk more about package and apps in the next section.
```

## Documentation

This directory can contain the following informations :
- Installation instruction
- Guidance and advices from project's developers
- Tutorials

## Assets

This directory will store all static files that needs to be shared within your project, but not relevant to the project internal features. This will include :
- Project's logos
- Documentation assets like :
  - Images
  - Demo videos
  - Schemas

## Scripts

This directory is where to place all non-python files, such as installation scripts or complexe [Makefile](../makefile) instructions. These can be :
- Dataset download
- Libraries build
- Environment setup

This is different from the [project's CLI commands](/package/cli/README.md), that will use package functions directly.

## Data

This directory will contain all project's data related files. This include `.csv`, images and other `.sqlite` file that you might use within your project.

## Tests

This module will contain you project's unit tests.

## Vscode config

Contains the configuration for recommmanded extensions as well as python settings for vscode's python project.


## Summary

This is what you should get when following this architecture :

```bash
ds_project_template/
├── .vscode/
│   ├── extension.json
│   └── launch.json
|   └── settings.json
├── apps/
│   ├── models/
│   └── website/
|   └── main.py
├── assets/
│   ├── images/
│   ├── languages/
│   ├── templates/
│   └── videos/
├── data/
├── documentation/
├── notebooks/
├── package/
│   ├── __init__.py
│   ├── cli/
│   ├── config/
│   ├── data/
│   ├── measures/
│   └── models/
├── tests/
├── scripts/
├── .env
├── .editorconfig
├── .flake8
├── .gitignore
├── pyproject.toml
├── Makefile
└── README.md
```
