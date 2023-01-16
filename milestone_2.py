import random


word_list = ['Banana', 'Avocado', 'Apple', 'Grapefruit', 'Grapes']
word = random.choice(word_list)
print(word)

guess = input('Please enter a single letter: ')

if len(guess) == 1 and guess.lower() >= 'a' and guess.lower() <= 'z'
