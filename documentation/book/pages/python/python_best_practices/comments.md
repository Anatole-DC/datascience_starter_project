# Comments

If you have been following the previous section, then you'll be surprised to ear that... you do not need comments !

It's one of the most confusing and outrageous claim I have been exposed with in my carrer, and yet it turned out to be true... It is aspecially confusing since so many teacher is computer science ask their students to place comments in their code. But [like docstrings](./docstring.md#L6), comments are almost never updated and therefore can be missleading ! This why experienced dev don't use comments (too much). [Here is a great video about the topic][code-aesthetic-no-comments].

So when to comment you may ask ?

## Pseudo-code

Use comments to layout the blueprint of your new function.

```python
def fizz_buzz(number: int) -> str:
  # Initialize an empty string

  # In a loop from 0 to the input number

    # When the number is 5, add fizz

    # When the number is 7 add buzz

    # When the number is odd add FizzBuzz

    # Else add the current number
  
  # Return the string
  ...
```

## Explain why you did the code this way

Use comments to explain a code decision, why you implemented this way, or what is it used for. Maybe it looks stupid but there is a good explanation behind that an other dev should be aware of.

```python
def a_very_obscure_function() -> float:
  ...
  # As it was my 10th attempt at this issue, I used ChatGPT to make it work.
  # This is the result of the prompt, it works, but I have no idea why...
  ...
```

[code-aesthetic-no-comments]: https://youtu.be/Bf7vDBBOBUA?feature=shared
