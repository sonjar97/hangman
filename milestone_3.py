import random


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

  check_guess(guess)
  
  
word_list = ['Banana', 'Avocado', 'Apple', 'Grapefruit', 'Grapes']
word = random.choice(word_list).lower()
print(word)

ask_for_input()
