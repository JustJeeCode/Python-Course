# Wordle game in Python

from collections import defaultdict
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
	

def check_guess(word, guess, guesses):
	letters = defaultdict(int)

	for letter in word:
		letters[letter] += 1

	if guess == word:
		for i in range(len(word)):
			board[guesses-1][i] = "🟩"
		return True
	else:
		for i in range(len(word)):
			if guess[i] == word[i]:
				letters[guess[i]] -= 1
				board[guesses-1][i] = "🟩"

		for i in range(len(word)):
			if guess[i] != word[i] and guess[i] in word and letters[guess[i]] > 0:
				letters[guess[i]] -= 1
				board[guesses-1][i] = "🟨"


def main():
	word = generate_word()
	guesses = 0
	is_running = True

	while is_running:
		display_board()
		guess = input("\nEnter a word to guess: ").upper()
		print()
		
		if not guess.isalpha() or len(guess) != len(word):
			print("That guess is invalid...\n")
			continue

		guesses += 1
		
		if check_guess(word, guess, guesses):
			display_board()
			if guesses == 1: print(f"\nCongratulations! You guessed the word. You got it in {guesses} guess.\n")
			else: print(f"\nCongratulations! You guessed the word. You got it in {guesses} guesses.\n")
			is_running = False

		if guesses >= 6:
			display_board()
			print(f"\nSorry, you have run out of guesses. The word was {word}.\n")
			is_running = False


if __name__ == "__main__":
	main()






	