# Type hints

Have you ever used your code editor, and when you put a dot after a variable to use one of its method, no autocompletion shows up ? It means your editor can't tell the type of the variable. It means you need to use **type hints**.

```{warning}
Type hints are not a true type inference. If you are storing an `int` within a variables that you have type-hinted as a `DataFrame`, my advice is that you take a good break from your work.
```

Use type hints whenever the return type of a variable is not explicit. Otherwise, it's not mendatory.

```python
my_dataset = DataFrame(...)     # Explicit type

# Sum could be int or float so we pass float hint to the variable to indicate the true return type
my_dataset_slice: float = DataFrame(...)["column"].sum()
```

Functions return types are almost always messed up by intellisense, so function type hints are always recommanded. Functions and methods parameters must **always be typed hinted**.

```
def my_function() -> int:
  ...
  return variable
```
