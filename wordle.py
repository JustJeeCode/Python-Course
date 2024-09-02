"""
Wordle game in Python

- Computer chooses a random word
- Player takes a guess
- Correct letters are highlighted
- Letters in the wrong place are highlighted
- Prompts again, repeats till player solves puzzle or fails

"""

import random


board = [["⬜", "⬜", "⬜", "⬜", "⬜"],
		 ["⬜", "⬜", "⬜", "⬜", "⬜"],
		 ["⬜", "⬜", "⬜", "⬜", "⬜"],
		 ["⬜", "⬜", "⬜", "⬜", "⬜"],
		 ["⬜", "⬜", "⬜", "⬜", "⬜"],
		 ["⬜", "⬜", "⬜", "⬜", "⬜"]]
guesses = []
randNum = random.randint(0, 5850)

# Picking a random number that is divisible by 5
while randNum % 5 != 0:
	randNum = random.randint(0, 5850)

randNum2 = randNum + 5

# Selecting a random word
with open("words.txt") as file:
	words = file.read()

word = words[randNum:randNum2]
print(word)

# Game loop
while True:
	for row in board:
		for element in row:
			print(element, end=" ")
		print()

	guess = input("Enter a word: ")
	guesses.append(guess)

	break

	# Detect which letters perfectly match up

	# Detect which letters are in the word but do not match up

	# Detect how many guesses there have been

	# Detect if the player has gotten the word right




