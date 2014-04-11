import string

class Board:

	def __init__(self):
		self.board = []
		self.board.append([0, 0, 0, 0, 0, 0, 0, 0,])
		self.board.append([0, 0, 0, 0, 0, 0, 0, 0,])
		self.board.append([0, 0, 0, 0, 0, 0, 0, 0,])
		self.board.append([0, 0, 0, 0, 0, 0, 0, 0,])
		self.board.append([0, 0, 0, 0, 0, 0, 0, 0,])
		self.board.append([0, 0, 0, 0, 0, 0, 0, 0,])
		self.board.append([0, 0, 0, 0, 0, 0, 0, 0,])
		self.board.append([0, 0, 0, 0, 0, 0, 0, 0,])

	def initialize_board(self, fen_string):
		rows = string.split(fen_string, '/')
		for row_index, row in enumerate(rows):
			# print row
			for index, character in enumerate(row):
				self.board[row_index][index] = character

"""rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"""
	