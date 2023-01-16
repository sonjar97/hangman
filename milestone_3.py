import random


word_list = ['Banana', 'Avocado', 'Apple', 'Grapefruit', 'Grapes']
word = random.choice(word_list)
print(word)

while True:
  guess = input('Please enter a single letter: ')
  if len(guess) == 1 and a.isalpha():
    break
  else:
    print('Invalid letter. Please, enter a single alphabetical character.')

if guess in word:
  print('Good guess! {} is in the word.'.format(guess)
else:
  print('Sorry, {} is not in the word. Try again.'.format(guess))








/*
You should use an if statement to check if the letter entered by the user is in the word. Remember that the input should be stored in a variable called "guess" and the randomly picked word should be stored in a variable called "word". You can use the "in" operator to check if a character is in a string. If you think you have done it correctly, remember to use the right indentation for the if statement and just a single space between the "if" keyword and the condition

Check whether the letter guessed by the user is in the secret word that was randomly chosen by the computer. For example, if the user guesses the letter "a" and the secret word is "apple", then your code should check if "a" is in "apple".

Step 1. Create an if statement that checks if the guess is in the word.

Step 2. In the body of the if statement, print a message saying "Good guess! {guess} is in the word.". Obviously, format the string to show the actual guess instead of {guess}.

Step 3. Create an else block that prints a message saying "Sorry, {guess} is not in the word. Try again." This block of code will run if the guess is not in the word.
*/
