# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Milestone 2
- Create a list of 5 fruits
- Import the random module and use the function choice() to randomly choose a fruit from the list
- Request user to input a single character and validate this input

### Python Code
```python
import random

word_list = ['Banana', 'Avocado', 'Apple', 'Grapefruit', 'Grapes']
word = random.choice(word_list)
print(word)

guess = input('Please enter a single letter: ')

if len(guess) == 1 and a.isalpha():
  print('Good guess!')
else:
  print('Oops! That is not a valid input.')
```

### Takeaways
- Use the isalpha() functin and not ASCII
- The random.choice() function comes in handy when selecting from an item

## Milstone 3
