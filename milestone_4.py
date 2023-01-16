import random


class Hangman:
  def __init__(self, word_list, num_lives=5):
    self.word_list = word_list
    self.num_lives = num_lives
    self.word = word = random.choice(word_list)
    
    self.word_guessed = ['_'] * len(word)
    self.num_letters = len(set(word.lower()))
    self.list_of_guesses = []
