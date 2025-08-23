# Enums

Enums are a lightweight datastructure to represent ordered values. They are very usefull when you want to abstract a raw value with code, and thus removing magic numbers.

```python
# Most awfull, what does 0 even represents ?
storage_method = 0

# Better, more readible, but what about lower-case, upper-case, value changes ?
storage_method = "csv"
```

Creating an enum is like creating a class.

```python
from enums import Enum

class StorageMethod(Enum):
  CSV = 0
  JSON = 1
  PARQUET = 2

method = StorageMethod.CSV
```

In this way, even if the values behind `CSV` or `JSON` changes, as the code will refer to it through an enum, it won't cause any bugs. 
