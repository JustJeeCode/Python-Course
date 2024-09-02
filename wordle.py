"""
Wordle game in Python

- Computer chooses a random word
- Player takes a guess
- Correct letters are highlighted
- Letters in the wrong place are highlighted
- Prompts again, repeats till player solves puzzle or fails

"""

import random


randNum = random.randint(0, 5850)
guesses = []


# Selecting a random number that is divisable by 5
while randNum % 5 != 0:
	randNum = random.randint(0, 5850)

randNum2 = randNum + 5


# Saving the text file words.txt as the variable words
with open("words.txt") as file:
	words = file.read()

word = words[randNum:randNum2]

print(word)

# Prompt user
while word not in guesses:
	guess = input("Enter in a word: ")

	if guess.upper() == word:
		print(f"That is correct the word was: {word}!")
		break
