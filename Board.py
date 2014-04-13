import string

class Board:

	def __init__(self):
		self.en_passant_target = ''
		self.half_move_clock = 0
		self.full_move_number = 0
		self.active_color = 'w'
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
			index = 0
			for character in row:
				if character.isdigit():
					index += int(character)
				else:
					self.board[row_index][index] = character
					index += 1

	def __unicode__(self):
		print self.board
		index = 0
		for row in self.board:
			
			index += 1
			print index

			row_string = ''
			for column in row:
				row_string += '[' + unicode(column) + ']'
			print row_string

"""rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"""
	