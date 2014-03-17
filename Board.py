import string

class Board:

	i = 12345

	def f(self):
		return 'hello world'

	def initializeBoard(self, fen_string):
		rows = string.split(fen_string, '/')
		for row in rows:
			print row

	def __init__(self):
		"""do nothing"""

"""rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"""
	