# Asserts

Working on code is like starting a project, **you want to fail fast**. The best way for this is to use `asserts`.

Imagine the following code :

```python
if not condition:
  raise Error("Message")

```

The code above using assert syntaxe :

```python
assert condition, "Message"
```

```{important}
Like clean code, start using asserts right away ! Don't think about adding them later, you won't !
```

You might ask yourselves, if nothing else but concise, why not use the first syntaxe only ? The reason is that asserts can be removed when building an optimized version of your project. [This stackoverflow thread](https://stackoverflow.com/a/1838411) explains it well.
