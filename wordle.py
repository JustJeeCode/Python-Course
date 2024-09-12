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
	word = []
	randNum = random.randint(0, 5850)

	while randNum % 5 != 0:
		randNum = random.randint(0, 5850)

	with open("words.txt") as file:
		words = file.read()

	return words[randNum:randNum+5]
	

def check_guess(guess, word):
	row = len(guesses)
	col = 0

	guesses.append(guess)
	word = list(word)
	guess = list(guess)
	result = ["", "", "", "", ""]

	if guess == word:
		for cell in board[row]:
			board[row][col] = "🟩"
			col += 1
		return "won"

	for letter in guess:
		if letter == word[col]:
			board[row][col] = "🟩"
			result[col] = "green"
		col += 1
	col = 0

	for letter in guess:
		if letter != word[col]:
			if letter in word:
				result[col] = "yellow"
			else:
				result[col] = "grey" 
		col += 1
	col = 0

	print(result)

	if len(guesses) == 6:
		return "lost"


word = "APPLE"
print(word)

while running:
	display_board()

	guess = ""
	while not guess.isalpha():
		guess = input(f"\n>>> ").upper()
	print()

	if guess == "Q":
		running = False

	checkGuess = check_guess(guess, word)

	if checkGuess == "won":
		display_board()
		print(f"\nCongratulations you guessed the word: {word}\nYou got the word in {len(guesses)} guesses!\n")
		running = False
	elif checkGuess == "lost":
		display_board()
		print(f"\nSorry, you used up all {len(guesses)} guesses...\nThe word was: {word}\n")
		running = False






	