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

	def __init__(self, *args, **kwargs):
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
		position_info = string.split(fen_string, ' ')
		rows = string.split(position_info[0], '/')
		for row_index, row in enumerate(rows):
			# print row
			index = 0
			for character in row:
				if character.isdigit():
					index += int(character)
				else:
					self.board[7 - row_index][index] = character
					index += 1

	def switch_player(self):
		if self.active_color == 'w':
			self.active_color = 'b'
		else:
			self.active_color = 'w'

	def move_piece(self, move_string):
		from_square = move_string[0:2]
		target_square = move_string[2:4]
		piece = self.find_square(from_square)

		correct_player = False
		if piece.islower():
			if self.active_color == 'b':
				correct_player = True
		else:
			if self.active_color == 'w':
				correct_player = True
		if correct_player:
			self.switch_player()
			self.find_square(from_square, 0)
			self.find_square(target_square, piece)
		else:
			print 'wrong player, biatch'

	def is_move_legal(self, move_string):
		from_square = move_string[0:2]
		target_square = move_string[2:4]
		piece = self.find_square(from_square)

		if piece == 'p' or piece == 'P':
			return self.check_pawn_move(from_square, target_square, piece)
		if piece == 'n' or piece == 'N':
			return self.check_knight_move(from_square, target_square, piece)
		if piece == 'b' or piece == 'B':
			return self.check_bishop_move(from_square, target_square, piece)
		if piece == 'r' or piece == 'R':
			return self.check_rook_move(from_square, target_square, piece)
		if piece == 'q' or piece == 'Q':
			return self.check_queen_move(from_square, target_square, piece)
		if piece == 'k' or piece == 'K':
			return self.check_king_move(from_square, target_square, piece)

	def check_pawn_move(self, from_square, target_square, piece):
		from_column = self.column_map[from_square[0]]
		from_row = self.row_map[int(from_square[1])]
		target_column = self.column_map[target_square[0]]
		target_row = self.row_map[int(target_square[1])]

		# pawn is advancing straight
		if abs(from_column - target_column) > 1:
			return False
		# pawns never move more than 2 spaces
		if abs(from_row - target_row) > 2:
			return False

		if from_column == target_column:
			# is pawn moving in right direction
			if piece == 'p':
				if from_row > target_row:
					# first move by pawn
					if from_row == 6:
						if from_row - target_row == 2 or from_row - target_row == 1:
							return True
					else:
						if from_row - target_row == 1:
							return True
				else:
					return False
			if piece == 'P':
				if target_row > from_row:
					# first move by pawn
					if from_row == 1:
						if target_row - from_row == 2 or target_row - from_row == 1:
							return True
					else:
						if target_row - from_row == 1:
							return True
				else:
					return False
		return False

	def check_bishop_move(self, from_square, target_square, piece):
		from_column = self.column_map[from_square[0]]
		from_row = self.row_map[int(from_square[1])]
		target_column = self.column_map[target_square[0]]
		target_row = self.row_map[int(target_square[1])]

		if abs(from_column - target_column) == abs(from_row - target_row):
			return True
		else:
			return False

	def check_knight_move(self, from_square, target_square, piece):
		from_column = self.column_map[from_square[0]]
		from_row = self.row_map[int(from_square[1])]
		target_column = self.column_map[target_square[0]]
		target_row = self.row_map[int(target_square[1])]

		if abs(from_column - target_column) == 1:
			if abs(from_row - target_row) == 2:
				return True
			else:
				return False
		elif abs(from_column - target_column) == 2:
			if abs(from_row - target_row) == 1:
				return True
			else:
				return False
		else:
			return False

		return True
	def check_rook_move(self, from_square, target_square, piece):
		from_column = self.column_map[from_square[0]]
		from_row = self.row_map[int(from_square[1])]
		target_column = self.column_map[target_square[0]]
		target_row = self.row_map[int(target_square[1])]

		if abs(from_column - target_column) > 0:
			if abs(from_row - target_row) > 0:
				return False
			else:
				return True
		if abs(from_row - target_row) > 0:
			if abs(from_column - target_column) > 0:
				return False
			else:
				return True

	def check_queen_move(self, from_square, target_square, piece):
		return (self.check_bishop_move(from_square, target_square) or 
						self.check_rook_move(from_square, target_square))

	def check_king_move(self, from_square, target_square, piece):
		from_column = self.column_map[from_square[0]]
		from_row = self.row_map[int(from_square[1])]
		target_column = self.column_map[target_square[0]]
		target_row = self.row_map[int(target_square[1])]

		return (abs(from_column - target_column) < 2 and 
				abs(from_row - target_row) < 2)

	def is_move_obstructed(self, from_square, target_square, piece):
		return False

	def find_square(self, square, replacement = None):
		column = self.column_map[square[0]]
		row = self.row_map[int(square[1])]

		current_piece = self.board[row][column]

		if replacement is not None:
			self.board[row][column] = replacement
		return current_piece

"""rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"""
	