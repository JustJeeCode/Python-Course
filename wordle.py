# Wordle game in Python

import random

# Variables
board = [["⬜", "⬜", "⬜", "⬜", "⬜"],
		 ["⬜", "⬜", "⬜", "⬜", "⬜"],
		 ["⬜", "⬜", "⬜", "⬜", "⬜"],
		 ["⬜", "⬜", "⬜", "⬜", "⬜"],
		 ["⬜", "⬜", "⬜", "⬜", "⬜"],
		 ["⬜", "⬜", "⬜", "⬜", "⬜"]]
guesses = []

# Word generator
randomWord = random.randint(0, 5850)

while randomWord % 5 != 0:
	randomWord = random.randint(0, 5850)

with open("words.txt") as file:
	words = file.read()

word = words[randomWord:randomWord+5]
print(word)

# Game loop
while True:
	for row in board:
		for element in row:
			print(element, end=" ")
		print()

	guess = input("Enter a word: ").lower()
	guesses.append(guess)

	if guess == word:
		print(f"You guessed the word in: {len(guesses)} attempt/s!")
		break



