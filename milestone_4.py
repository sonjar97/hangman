import random


class Hangman:
  def __init__(self, word_list, num_lives=5):
    self.word_list = word_list
    self.num_lives = num_lives
    self.word = word = random.choice(word_list)
    
    self.word_guessed = ['_'] * len(word)
    self.num_letters = len(set(word.lower()))
    self.list_of_guesses = []
    
  def check_guess(self, guess):
    guess = guess.lower()
    if guess in self.word:
      print('Good guess! {} is in the word.'.format(guess))
      self.list_of_guesses.append(guess)
  
  
  def ask_for_input(self):
    i = 0
    while i < 7:
      guess = input('Please enter a single letter: ').lower()
      if not (len(guess) == 1 and guess.isalpha()):
        print('Invalid letter. Please, enter a single alphabetical character.')
      elif guess in self.list_of_guesses:
        print('You already tried that letter!')
      else:
        self.check_guess(guess)
      i++
