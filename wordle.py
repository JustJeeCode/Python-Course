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

	word = words[randNum:randNum+5]

	return word
	

def check_guess(guess, word):
	row = len(guesses)
	col = 0

	guesses.append(guess)
	word = list(word)
	guess = list(guess)
	amountOfLetters = {}

	for letter in word:
		amount = word.count(letter)
		amountOfLetters.update({letter: amount})

	# if guess is correct
	if guess == word:
		for cell in board[row]:
			board[row][col] = "🟩"
			col += 1
		return "won"

	# if guess is incorrect and x letters are correct
	for letter in guess:
		if letter == word[col]:
			board[row][col] = "🟩"
		col += 1
	col = 0

	# if guess is incorrect and x letters are in the incorrect spot
	for letter in guess:
		if letter != word[col] and letter in word:
			if amountOfLetters[letter] > 0:
				board[row][col] = "🟨"
				amountOfLetters[letter] -= 1
		col += 1
	col = 0

	print(amountOfLetters)

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






	