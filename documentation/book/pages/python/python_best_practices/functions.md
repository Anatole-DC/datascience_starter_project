# Functions

Function size should not exceed 60 lines ([according to NASA power of 10's 4th rule](https://en.wikipedia.org/wiki/The_Power_of_10:_Rules_for_Developing_Safety-Critical_Code)).

Given the same parameters, the function should always produce the same outputs to avoid unpredicted behavior.

The function should always return the same type for each return statement within it.

## Improve readability

Functions are a great way to make your code more readable ! Let's see an example.

We have an `access_file` function. It takes a user and a file in inputs. It must check if the file exists, if the user is allowed to view the file, and if so, return the file content.

```python
def access_file(user: User, file: File) -> str:
  if not file.path.exists():
    raise FileNotFound("The file requested was found")
  if user.authorization != file.authorization:
    raise Exception("User not allowed to access this file")
  
  file_content: str = ""
  with open(file.path) as file_reader:
    file_content = file_reader.read()
  
  return file_content
```

In the above exemple, all the code is written in the same function. Although concise, it affects readability.

To improve it, we will isolate each function's behavior within a smaller function.

```python
def check_file_validity(file: File) -> None:
  if not file.path.exists(): raise FileNotFound("The file requested was found")

def check_user_file_permission(user: User) -> None:
  if user.authorization != file.authorization: raise Exception("User not allowed to access this file")

def read_file_content(file: File) -> str:
  file_content: str = ""
  with open(file.path) as file_reader:
    file_content = file_reader.read()
  return file_content

def access_file(user: User, file: File) -> str:
  check_file_validity(file)
  check_user_file_permission()
  return read_file_content(file)
```

Although we have written more code, the function we are interested in (the `access_file` function), is now more readable. Another advantage is that we can now improve individual parts way more easily.

What we just did is called code refactoring. And we will talk about it later on.

```{note}
If you are planning your functions with pseudo-code, you could just replace your comments by actual function names, and implement them one by one. This way, your main function will already be cleaner.
```
