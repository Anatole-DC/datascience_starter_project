# Pathlib

[Pathlib](https://docs.python.org/3/library/pathlib.html) is a python's native library, allowing to greatly simplify path handling and usages.

> TL,DR : you don't need to use `os.join`, `os.path`, etc... anymore.

To use it, you must instantiate a `Path` class, with your absolute or relative path as parameter.

**How to know if a path is a directory, a file, or even if it exists :**

Without pathlib :

```python
import os

my_path = "my_path"

os.path.exists(my_path)
os.path.isfile(my_path)
os.path.isdir(my_path)
```

With pathlib :

```python
from pathlib import Path

my_path = Path("my_path")

my_path.exists(my_path)
my_path.isfile(my_path)
my_path.isdir(my_path)
```

**Join paths**

Without pathib :

```python
import os

my_path = "my_path"
sub_my_path_1 = "my_path"
sub_my_path_2 = "my_path"

os.path.join([my_path, sub_my_path_1, sub_my_path_2])
```

With pathlib :

```python
from pathlib import Path

my_path = Path("my_path")
sub_my_path_1 = "my_path"
sub_my_path_2 = "my_path"

my_path / sub_my_path_1 / sub_my_path_2     # Like in your terminal
```

**Directory navigation**

Without pathlib :

```python
import os

my_path = "my_path"

os.path.abspath(my_path)                     # Absolute path
os.path.dirname(my_path)                     # Parent directory
os.path.basename(my_path)                    # Path last element's name
os.path.splitext(file_name)[0]               # Filename without extension
os.path.basename(os.path.basename(my_path))  # Navigate up two directories
```

With pathlib :

```python
from pathlib import Path

my_path = Path("my_path")

my_path.absolute()       # Absolute path
my_path.parent           # Parent directory
my_path.name             # Path last element's name
my_path.stem             # Filename without extension
my_path.parent.parent    # Navigate up two directories
```
