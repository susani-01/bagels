import random

NUM_DIGITS = 3
MAX_GUESSES =10

def main():
	print("""
		I am thinking of a {}-digit number with no repeated digits.
		Try to guess what is there.Here are some clues: 
		When I say:		That means:

		Pico			One digits is correct but in the wrong position.
		Fermi			One digits is correct and in the right position.
		Bagels 			No digit is correct.



		For example if the secret number was 248 and your guess was 843, the Clues would be Fermi Pico """.format(NUM_DIGITS))

	while True:
		"""This store the secret number the player needs to guess: """
		secretNum = getSecretNum()
		print('I have thought up a number.')
		print ('You have {} guesses to get it.'.format(MAX_GUESSES))

		numGuesses =1
		while numGuesses <= MAX_GUESSES:
			guess = ' '

			while len(guess) != NUM_DIGITS or not guess.isdecimal():
				print('Guess #{}: '.format(numGuesses))
				guess = input('> ')


			clues = getClues(guess, secretNum)
			print(clues)
			numGuesses += 1

			if guess == secretNum:
				break

			if numGuesses >MAX_GUESSES:
				print('You ran out of the guesses.')
				print('The answer was {}.'.format(secretNum))

			#Ask the player if they want to play again

		Print('Do you want to play Again? (yes or no)')
		if not input('> ').lower().startswith('y'):
			break

		print('Thanks for playing! ')

def getSecretNum():
	"""Return a string made up of NUM_DIGITS unique random digits."""
	numbers = list('0123456789')
	random.shuffle(numbers)

	secretNum = ' '
	for i in range(NUM_DIGITS):
		secretNum += str(numbers[i])

	return secretNum

def getClues(guess,secretNum):
	"""Returns a string with the pico,fermi,bagels clues for a guess and secret number pair."""
	if guess == secretNum:
		return 'You got it! '

	clues = []

	for i in range(len(guess)):
		if guess[i]==secretNum[i]:
			clues.append('Ferm')
		elif guess[i] in secretNum:
			clues.append('Pico')

	if len(clues)==0:
		return 'Bagels'

	else:
		clues.sort()
		return ' '.join(clues)

#if the program is run (instrea of imported ),run the game:
if __name__=='__main__':
	main()
	