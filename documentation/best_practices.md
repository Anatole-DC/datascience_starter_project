# Best practices

This document gives advices on how to develop good code.

> Note that they do not stand as absolute rules, and more as coding advices ! If you have your own set of rules, feel free to use them instead !

## Summary

- [Best practices](#best-practices)
  - [Summary](#summary)
  - [Code](#code)
    - [Naming conventions](#naming-conventions)
      - [Variables](#variables)
      - [Functions](#functions)
      - [Classes](#classes)
      - [Modules](#modules)
    - [Functions](#functions-1)
    - [Type hints](#type-hints)
    - [Comments](#comments)
    - [Environment variables](#environment-variables)
  - [Git](#git)
    - [Naming conventions](#naming-conventions-1)
      - [Branches](#branches)
      - [Commit](#commit)
    - [Commit content](#commit-content)
  - [Code quality](#code-quality)
  - [Project workflow](#project-workflow)


## Code

### Naming conventions

Most important rule for naming is **Keep your naming rules consistent** !

Here are some of the rules that apply to each named element within your code :
- Do not use abbreviations ;
- Use explicit names ;
- Do not include variable type inside name (prefer [type hints](#type-hints)) ;
- **Do not use language's keywords as name** ;

#### Variables

Prefer `snake_case`.

```python
my_variable_name = 5
```

#### Functions

Also prefer `snake_case`.

```python
def my_function_name():
    ...
```

#### Classes

Prefer `CamelCase`.

```python
class MyClassName:
    ...
```

#### Modules

Prefer `snake_case`. Include parent module name for submodules except for `utils` and `helpers` submodules.

```bash
module_name/
    utils/
        some_utilities.py
    module_submodule_name.py
    ...
```

### Functions

Function size should not exceed 60 lines (according to NASA).

Although they can be extremely useful, beware of the function docstrings. Developer don't often think about updating them. If you write function doctstrings, think about updating it when you are updating the function source code !

Given the same parameters, the function should always produce the same outputs to avoid unpredicted behavior.

The function should aways return the same type.

### Type hints

Use type hints whenever the return type of a variable is not explicit. Otherwise, it's not mendatory.

```python
my_dataset = DataFrame(...)     # Explicit type

# Sum could be int or float so we pass float hint to the variable to indicate the true return type
my_dataset_slice: float = DataFrame(...)["column"].sum()
```

Functions return types are almost never caught by intellisense, so function type hints are always recommanded. Functions and methods parameters must **always be typed hinted**.

```python
def add_two_ints(a: int, b: int) -> int:
    return a + b
```

You can defined custom types the same way you declare variables

```python
# This function uses the same type for each parameter and return statement
def add_two_numbers(a: int | float, b: int | float) -> int | float:
    return a + b

# Declare a new Number type for better lisability
Number = int | float
def add_two_numbers(a: Number, b: Number) -> Number:
    return a + b
```

Use the typing module for `List` and `Dict`.

```python
from typing import List, Dict

# Wrong way of doing things
my_list_of_ints: list = [1, 2, 3, 4, 5]
my_str_dict: dict = {"key": "value"}
my_float_dict: dict = {"key": 5.0}

# Correct way
my_list_of_ints: List[int] = [1, 2, 3, 4, 5]
my_str_dict: Dict[str, str] = {"key": "value"}
my_float_dict: Dict[str, float] = {"key": 5.0}
```

### Comments

Prefer comments that explain why the code was coded this way, rather than a comment explaining what the code does.

In the following code, the comment is useless, as the variables and methods name are explicit enough.

```python
my_column = my_dataset["column"]

# Compute the mean of a column
my_column_mean: float = my_column.mean()
```

### Environment variables

Whenever you try to work with :
- User specific informations, like file path
- Variables that can change from one system to another
- Informations that you would not give to your neighbourgs
You are probably in need of environment variables.

Store them in a `.env` file at the root of your project.

**DO NOT PUSH `.env` FILE ON GITHUB !!!**

You can create and push a `.env.template` file that will contain all the variables that the users need to write themselves in order to start using your project.

## Git

### Naming conventions

#### Branches

Your branch name should explain most of the work you are planning to do. Examples :

```bash
feat/implement-data-preprocessing
fix/solve-wrong-numbers-of-units-in-lstm
doc/add-deployement-documentation
refact/clean-data-processing-function
```

#### Commit

Same as branch, indicate the scope of your commit. If additional explaination are needed, don't forget about the commit description !

```bash
commit -m "feat(preproc): add new preprocessing function"

commit -m "doc(preproc): improve the preprocessing doc" -m "Added new preprocessing behavior in the documentation, and update old doc for CLI commands"
```

### Commit content

Limit the usage of `git add .`. Prefer using your code architecture to add features that are similar.

```bash
git add package/data/   # Will add all data related updates
```

If the updates are spreaded arround your projects, use vscode's source control to add files manually.

## Code quality

Use tools like [editorconfig](https://editorconfig.org/), [black](https://black.readthedocs.io/en/stable/) and [flake8](https://flake8.pycqa.org/en/latest/) to ensure your code format stays the same for all code contributors.

```bash
black .
flake8

# Simplified version
make code-clean
```

## Project workflow

You should aim at implementing a full workflow as soon as possible. None of the features within this first workflow need to be perfect. The goal is to produce a production chain that can be improved through iterative work.
