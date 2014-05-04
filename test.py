from Chess import Board

board = Board()

board.initialize_board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')
board.move_piece('e2e4')
board.move_piece('e7e5')
board.move_piece('g1f3')
board.move_piece('b8c6')
# board.initialize_board('rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR')
# print unicode(board)
for row in reversed(board.board):
	row_string = ''
	for column in row:
		row_string += unicode(column) + ' '
	print unicode(row_string)