# Docstring

Docstring are displayed when hovering on you code elements within your code editor. In python, it's only for functions, classes and modules, but other languages (like go) allow variable docstring.

```{attention}
Since we work mostly on code and not documentation, docstrings are often less updated, thus sometime missleading ! Try to avoid too technical details within them, as it might become false later on !
```

In python, a docstring is written like this :

```python
"""
  Place your docstring here.
"""
```

> Yes, many people use this syntaxe to comment large chunks of code, but I would argue that they would be better off finding how to comment multiple lines at once...

## Function docstring

Here is the syntaxe for function docstring.

```python
def my_function():
  """
    This is my function's docstring.
  """
  ...
```

```{admonition} Tip !
Use [autoDocstring](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring) to generate docstrings automatically.
```

## Module docstring

Use the docstring syntaxe at the top of any python file. It will be displayed when hovering on the import of said python file.
