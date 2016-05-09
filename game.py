from random import choice
from itertools import product
class Board:
	def __init__(self, size = 4, maxAttempts = 10):
		self.size = size
		self.maxAttempts = maxAttempts
		self.solution = "".join(choice(list(product('RYBGOV',repeat=self.size))))
		self.clueHistory = []
		self.nbTries = 0
	def trySolution(self, guess):
		if self.nbTries == self.maxAttempts:
			return -1
		self.nbTries += 1
		if self.solution == guess:
			return 1
		else:
			clue = ['B' if guess[i] == self.solution[i] else 'W' if (guess[i] in self.solution and guess[i] != self.solution[i]) else 'Z' for i in range(self.size)]
			clue.sort()
			clue = "".join(clue)
			self.clueHistory.append(clue)
			return clue


if __name__ == '__main__':
	attempts = 0
	success = 0
	game = Board()
