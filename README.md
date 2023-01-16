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
- Create two functions. One that that checks if the guessed letter is in the word and one that asks the user to guess a letter

### Python Code
```python
def check_guess(guess):
  guess = guess.lower()
  
  if guess in word:
    print('Good guess! {} is in the word.'.format(guess))
  else:
    print('Sorry, {} is not in the word. Try again.'.format(guess))
    
    
def ask_for_input():
  while True:
    guess = input('Please enter a single letter: ')
    if len(guess) == 1 and guess.isalpha():
      break
    else:
      print('Invalid letter. Please, enter a single alphabetical character.')
```

### Takeaways
- Functions are used to carry out a specific task
- Functions also make the code more readable and accessible
