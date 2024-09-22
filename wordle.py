# Wordle game in Python

import random


board = [["⬜", "⬜", "⬜", "⬜", "⬜"],
		 ["⬜", "⬜", "⬜", "⬜", "⬜"],
		 ["⬜", "⬜", "⬜", "⬜", "⬜"],
		 ["⬜", "⬜", "⬜", "⬜", "⬜"],
		 ["⬜", "⬜", "⬜", "⬜", "⬜"],
		 ["⬜", "⬜", "⬜", "⬜", "⬜"]]


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
	correctLetters = []

	if guess == word:
		return True
	else:
		# iterate through every letter in our guess
		# if our letter matches with the guess letter add it to the list as True
		# if the letter doesn't match the guess letter add it to the list as False





def main():
	word = generate_word()
	guesses = 0
	running = True

	print(word)

	while running:
		display_board()
		guess = input("\nEnter a word to guess: ").upper()
		
		if not guess.isalpha() or not len(guess) == 5:
			print("\nThat guess is invalid.\n")
			continue

		guesses += 1
		check_guess(guess, word)

		if check_guess(guess, word) == True:
			print(f"\nCongratulations! You guessed the word. You got it in {guesses} guesses.")
			break
		else:
			print(check_guess(guess, word))
			break


if __name__ == "__main__":
	main()










	