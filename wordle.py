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


def generate_word():
	randNum = random.randint(0, 5850)

	while randNum % 5 != 0:
		randNum = random.randint(0, 5850)

	with open("words.txt") as file:
		words = file.read()

	return words[randNum:randNum+5]
	

def check_guess(guess):
	col = 0
	row = len(guesses)
	guesses.append(guess)

	# if the guess = the word
	if guess == word:
		for letter in board[row]:
			board[row][col] = "🟩"
			col += 1
		return "won"

	# check for correct letters
	for letter in guess:
		if letter == word[col]:
			board[row][col] = "🟩"
		col += 1

	# check for incorrect positions
	for letter in guess:
		if board[row][col] != "🟩"
			# check if that letter is in the word
			# if it is and it isn't a previous letter turn it yellow


	# if player used all guesses
	if len(guesses) == 6:
		return "lost"


word = "APPLE"

while running:
	print(word)
	display_board()

	guess = ""
	while not guess.isalpha() or len(guess) != 5:
		guess = input(f"\n>>> ").upper()
	print()

	result = check_guess(guess)

	if result == "won":
		display_board()
		print(f"\nCorrect the word was {word}!\nYou got it in {len(guesses)} guesses!")
		running = False
	elif result == "lost":
		display_board()
		print(f"\nIncorrect, you used all {len(guesses)} guesses...\nThe word was {word}.\n")
		running = False






	