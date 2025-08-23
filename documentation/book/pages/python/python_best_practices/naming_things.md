# Naming things

Most important rule for naming is **Keep your naming rules consistent** ! Almost all the remaining advices in this document can be different from one project to the other, but consistency is the one point all good code project have in common.

As you gain experience, you will use your own set of rules. For good rules, keep in mind that writing code may take long, but understand it later on will take longer. Therefore, you want your code to be as clear as possible.

## How to name

Here are some of the rules that apply to each named element within your code.

### Do not use abbreviations

Abbreviations are often related to buisiness cases, and may not speak to everyone reading your code. Use full names. Although they are longer to write, they will be easier to read.

### Use explicit names

Avoid named with a single character when possible. Exceptions for this are :
- `i` and `j` for numerical index within loops ;
- `x`, `y` and `z` for coordinates ;
- `r`, `g` and `b` for colors channels ;

Do not shorten words within your names.

```python
bob = Individual(...)

# Don't
bob.s    # Is .s refering to individual sex, status ?

# Do
bob.status
```

### Prefer type hints over plain types in name.

Code editor are displaying types for you. When you can, avoid putting the type name within the name. Aspecially if the expected type is explicit.

```python
# Don't
config_path = Path("path/to/my/config")   # We can clearly see that config is a path

# Just do
config = Path("path/to/my/config")
```

When the type is not explicit prefer [type hints](#type-hints).

Exception can be made for situations were multiple variables are used for one concept. For instance in a file read.

```python
file_path = Path("file")

with open(file_path) as file_reader:
  # Perform action on the file reader
  file_reader.read()
```

In the above exemple, only using the word `file` would lead to confusion to separate the reader and the path. Therefore, we use the explicit type within the name.

### Do not use language's keywords as name

At best, you will only get a runtime error.

```python
# Don't
def = "A word definition."

# Do
definition = "A word definition."
```

In the above exemple, we use the word `def` to store a definition. But the `def` keyword is reserved to declare python functions.

> You will note that using [the not abbreviation rule](#do-not-use-abbreviations) prevent the error aboved.

```{warning}
Be careful not to name a variable with the same name you used for a python function ! This will cause the function to be overwritten by the variable !
```

## Case

You want to keep a consistent case for your element type as well. Here are rules that are generally applied in python.

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
