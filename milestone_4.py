import random


class Hangman:
  def __init__(self, word_list, num_lives=5):
    self.word_list = word_list
    self.num_lives = num_lives
    
    self.word_list = ['Banana', 'Avocado', 'Apple', 'Grapefruit', 'Grapes']
    self.word = word = random.choice(word_list).lower()
    
    self.word_guessed = []
    self.num_letters = 100
    self.list_of_guesses = []
