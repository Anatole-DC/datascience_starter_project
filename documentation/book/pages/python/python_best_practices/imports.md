# Imports

Always import what you need. In other words, instead of :

```python
import module
```

Prefer :

```python
from module import element
```

Imported elements should always be :
- classes
- functions
- constants

```{danger}
**Do not write `from module import *` !**
```

## Import order

In order to keep your code consistent, the import should be written in this order, with one line between each section :
1. python native elements
2. installed libraries elements
3. your custom local module elements

```python
from pathlib import Path
from os import environ

from pandas import DataFrame


from my_library import my_function
```

## Import aliases

Import aliases can becomme useful when you are importing :
- A function with a similar name than one of your already imported function
- When the imported function's name lacks clarity

```python
from rich import print as rich_print
```

In the above code, you might don't want to override python's `print` function...
