from random import choice
from itertools import product

class Board:
	def __init__(self, size = 4, maxAttempts = 10):
		self.size = size
		self.colors = 'RYBGOV'
		self.maxAttempts = maxAttempts
		self.solution = "".join(choice(list(product(self.colors,repeat=self.size))))
		self.clueHistory = []
		self.nbTries = 0

	def trySol(self, guess):
		if len(guess) != self.size:
			raise ValueError('Invalid guess length')

		if self.nbTries == self.maxAttempts:
			return -1
		self.nbTries += 1
		if self.solution == guess:
			return 1
		else:
			clue = ""
			remainingSecret = []
			remainingGuess = []
			for secret,attempt in zip(self.solution, guess):
				if secret == attempt:
					clue += 'B'
				else:
					remainingGuess.append(attempt)
					remainingSecret.append(secret)

			for attempt in remainingGuess:
				if attempt in remainingSecret:
					clue += 'W'
					remainingSecret.remove(attempt)
				else:
					clue += 'Z'

			clue = "".join(sorted(clue))
			self.clueHistory.append(clue)
			return clue

	def autoSolve(self):
		allSolutions = list(product(self.colors,repeat=self.size))
		initAttempt = 'RRYY'
		reponse = self.trySol(initAttempt)


if __name__ == '__main__':
	attempts = 0
	success = 0
	game = Board()
