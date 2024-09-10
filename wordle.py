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
	if guess == word:
		for element in board[currentRow]:
			board[currentRow][currentCol] = "🟩"
			currentCol += 1
		print()
		display_board()
		print(f"\nCorrect the word was {word}!\nYou got it in {len(guesses)+1} guesses!")
		return "won"

	elif guess != word:
		guesses.append(guess)

		# Check if the guess has any correct letters in the word

		# Check if the letters are in the correct spot

		# Check if the letters are in the wrong spot

		if len(guesses) >= 6:
			print(f"\nIncorrect, you used all {len(guesses)} guesses...\nThe word was {word}.\n")
			return "lost"



while running:
	display_board()

	word = random_word()
	print(word)

	guess = input(f"\n>>> ").upper()
	result = guess_checker(guess, currentRow=len(guesses), currentCol=0)

	if result == "won" or result == "lost":
		running = False

	







