# Package vs Apps

The first question you must ask yourself when developping your project is this : Is this going in an app, or in my package ?

The awnser for this is simple. If the code might be used by multiple apps, it's going in the package.

## Package

The inside structure of a python package, although quite permissive, should also be well organized. From this organization, depends how easy it will be to use the package.

### New feature

When you are developping a feature, you should think about how will the feature be used. This will determine :
- Where you will store the feature ;
- How you will name the feature ;

You should also ask yourself what is the feature's scope :
- What should it do ?
- What shouldn't it do ?

```python
from pandas import DataFrame

def save_data(data: DataFrame, output_file: Path) -> Path:
  output_directory.parent.mkdir(parents=True, exists_ok=True)
  
  data.to_csv(output_file)

  print(f"The file was saved at path {output_file.absolute()}")

  return output_file
```

The above function performs three actions before returning the `output_file` path. :
- It creates the `output_file`'s parent if it does not exist ;
- It saves the data ;
- It prints a message ;

There is nothing wrong is this function, but we could've ask ourselved these questions :
- Is this the role of this function to handle the output's parent creation ?
- Would the print message be better placed outside this function ?

```{admonition} Tip !
When you are moving a feature outside a function, you can still use an `assert` to ensure everything is still working well.
```

### Pro usage of `__init__.py`

Since a version of python, the `__init__.py` is not mendatory for a module to be a package. However, this file is still very useful, since it allows you to clean your module exports. Let me explain.

You have the following architecture for a `preprocessing` package :

```
working_directory/
├── main.py
├── preprocessing/
│   ├── preprocessing_machine_learning.py
│   └── preprocessing_deep_learning.py
```

In the `main.py` you can import your function like this :

```python
from preprocessing.preprocessing_machine_learning import preproc as ml_preproc
from preprocessing.preprocessing_deep_learning import preproc as dl_preproc
```

Although is works, we could improve it so that all preprocessing functions are grouped within the same import name. However, we still want to keep our machine learning and deep learning preprocessing in separate files. To do this, we can add a `__init__.py` file inside our `preprocessing` module.

```
working_directory/
├── main.py
├── preprocessing/
│   ├── __init__.py
│   ├── preprocessing_machine_learning.py
│   └── preprocessing_deep_learning.py
```

When we will do `import preprocessing`, it will actually import the code within the `__init__.py` file. Therefore, we can do all of our relevant imports in this file.

```python
from .preprocessing_machine_learning import preproc as ml_preproc
from .preprocessing_deep_learning import preproc as dl_preproc
```

And now within the `main.py` file, we can write our imports like this :

```python
from preprocessing import ml_preproc, dl_preproc
```

## Apps

In this directory, you will create a directory for :
- APIS (with Flask or FastAPI) ;
- Interfaces (with Streamlit) ;
- Single scripts to test your code ;

```{note}
There is a real interest in storing all your apps in the same project working directory. We will talk more about this when talking about [monorepos]().
```
