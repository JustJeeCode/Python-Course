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
running = True


def display_board():
	for row in board:
		for element in row:
			print(element, end=" ")
		print()


def random_word():
	randNum = random.randint(0, 5850)

	while randNum % 5 != 0:
		randNum = random.randint(0, 5850)

	with open("words.txt") as file:
		words = file.read()

	return words[randNum:randNum+5]
	

def guess_checker(guess):
	if guess == word:
		print(f"\nCorrect the word was {word}!")
		return "won"

	elif guess != word:
		guesses.append(guess)

		if len(guesses) >= 6:
			print(f"\nIncorrect, you have run out of guesses...\nThe word was {word}.")
			return "lost"



while running:
	display_board()

	word = random_word()
	print(word)

	guess = input(f"\n>>> ").upper()
	result = guess_checker(guess)

	if result == "won" or result == "lost":
		running = False

	







