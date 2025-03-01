# Project refactoring

As you develop your project, it will grow in size and you might need to refactor the code.

**DO NOT WAIT FOR THE SITUATION TO BE AWFUL TO START REFACTORING !!!**

## When to refactor

- When a file grows too large
- When a function lacks readability
- When a code is slow
- When feature/fixes are hard to implement

## How to refactor

Imagine you have a very large python module file. Follow this process :
1. Create a directory with the name of the module
2. Split each function of the origin file into individual python file within you directory
3. Split unclear function parts into smaller functions with clear name
4. Create a `__init__.py` file in the directory
5. Import the main function from each of the new individual files

> This will produce more files, but they will self contain all utilities function.  
> Using the same name for the directory will also ensure your links are not broken.
