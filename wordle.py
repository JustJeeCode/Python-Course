# Wordle game in Python

import random


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
	

def guess_checker(guess, currentRow, currentCol):
	guesses.append(guess)

	print()

	if guess == word:
		for element in board[currentRow]:
			board[currentRow][currentCol] = "🟩"
			currentCol += 1

		display_board()
		print(f"\nCorrect the word was {word}!\nYou got it in {len(guesses)} guesses!")
		return "won"

	elif guess != word:
		for letter in guess:
			if letter in word:
				board[currentRow][currentCol] = "🟨"

			if letter == word[currentCol]:
				board[currentRow][currentCol] = "🟩"

			currentCol += 1

		if len(guesses) >= 6:
			display_board()
			print(f"\nIncorrect, you used all {len(guesses)} guesses...\nThe word was {word}.\n")
			return "lost"


word = random_word()

while running:
	display_board()

	guess = ""
	while not guess.isalpha() or len(guess) != 5:
		guess = input(f"\n>>> ").upper()

	result = guess_checker(guess, currentRow=len(guesses), currentCol=0)

	if result == "won" or result == "lost":
		running = False

	