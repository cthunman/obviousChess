import string, math

class Board:

	column_map = {
		'a' : 0,
		'b' : 1,
		'c' : 2,
		'd' : 3,
		'e' : 4,
		'f' : 5,
		'g' : 6,
		'h' : 7,
	}
	row_map = {
		1 : 0,
		2 : 1,
		3 : 2,
		4 : 3,
		5 : 4,
		6 : 5,
		7 : 6,
		8 : 7,
	}

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
					self.board[7 - row_index][index] = character
					index += 1

	def move_piece(self, move_string):
		from_square = move_string[0:2]
		target_square = move_string[2:4]
		piece = self.find_square(from_square, 0)
		self.find_square(target_square, piece)

	def is_move_legal(self, move_string):
		from_square = move_string[0:2]
		target_square = move_string[2:4]
		piece = self.find_square(from_square)
		
		from_column = self.column_map[from_square[0]]
		from_row = self.row_map[int(from_square[1])]
		target_column = self.column_map[target_square[0]]
		target_row = self.row_map[int(target_square[1])]

		if piece == 'p':
			# pawn is advancing straight
			if from_column == target_column:
				# is pawn moving in right direction
				if from_row > target_row:
					# first move by pawn
					if from_row == 6:
						if from_row - target_row == 2:

				else:
					return False


	def find_square(self, square, replacement = None):
		column = self.column_map[square[0]]
		row = self.row_map[int(square[1])]

		current_piece = self.board[row][column]

		if replacement is not None:
			self.board[row][column] = replacement
		return current_piece

"""rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"""
	