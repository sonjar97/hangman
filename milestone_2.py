import random


word_list = ['Banana', 'Avocado', 'Apple', 'Grapefruit', 'Grapes']
word = random.choice(word_list)
print(word)

guess = input('Please enter a single letter: ')

if len(guess) == 1 and a.isalpha():
  print('Good guess!')
else:
  print('Oops! That is not a valid input.')
