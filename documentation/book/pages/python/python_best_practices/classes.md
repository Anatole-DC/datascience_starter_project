# Classes

Although all of the code can be written using functions, classes are very useful to implement re-usable or adaptable components within our code. Some language (like previous version of Java) even only use classes.

Classes are very handy to implement what we call design patterns. You can have a look at [this amazing website][refactoring-guru] if you want to learn more about design patter.

I won't dive into deeper details about classes since it depends a lot of coding culture (which design pattern one prefers, etc...). However, classes can be useful for easier data representation.

```python
word_apple = {
  "name": "apple",
  "definition": "It's a fruit.",
  "exemple": "An apple a day keep the doctor away."
}

# This can be done
word["address"] = "61 rue Servan, 75011 PARIS"
```

In the above code, a word is represented by a dictionnary. This structure is not very stable as one could decide to add an extra field to the dictionnary. We can use classes to make sure the data structure is more stable.

```python
class Word:
  def __init__(self, name: str, definition: str, exemple: str | None):
    self.name = name
    self.definition = definition
    self.exemple = exemple
  
  # Implement the rest of the logic there

  ...

apple = Word("apple", "It's a fruit", "An apple a day keep the doctor away.")
```

```{admonition}
In the realm of data, this can be very useful when we want to give our data structure mathematical meaning (with `sum` etc...). We only have to implement the method in the class, and we are good to go.
```






[refactoring-guru]: https://refactoring.guru/fr
