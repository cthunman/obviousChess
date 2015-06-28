from Chess import Board

board = Board()

board.initialize_board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')

# if board.is_move_legal('e2e4'):
# 	board.move_piece('e2e4')
# 	for row in reversed(board.board):
# 		row_string = ''
# 		for column in row:
# 			row_string += unicode(column) + ' '
# 		print unicode(row_string)
# 	print '\n'
# else:
# 	print 'not legal or not defined'

# if board.is_move_legal('e7e5'):
# 	board.move_piece('e7e5')
# 	for row in reversed(board.board):
# 		row_string = ''
# 		for column in row:
# 			row_string += unicode(column) + ' '
# 		print unicode(row_string)
# 	print '\n'
# else:
# 	print 'not legal or not defined'

# if board.is_move_legal('g1f3'):
# 	board.move_piece('g1f3')
# 	for row in reversed(board.board):
# 		row_string = ''
# 		for column in row:
# 			row_string += unicode(column) + ' '
# 		print unicode(row_string)
# 	print '\n'
# else:
# 	print 'not legal or not defined'

# if board.is_move_legal('b8c6'):
# 	board.move_piece('b8c6')
# 	for row in reversed(board.board):
# 		row_string = ''
# 		for column in row:
# 			row_string += unicode(column) + ' '
# 		print unicode(row_string)
# 	print '\n'
# else:
# 	print 'not legal or not defined'


while True:
    text = raw_input()
    if text =='':
    	continue
    elif board.is_move_legal(text):
    	board.move_piece(text)
    	for row in reversed(board.board):
    		row_string = ''
    		for column in row:
    			if column == 0:
    				row_string += '_' + ' '
    			else:
    				row_string += unicode(column) + ' '
    		print unicode(row_string)
    	print '\n'
    else:
    	print text + ' not legal or not defined'

# e2e4
# e7e5
# g1f3
# b8c6
# g8f6
# b1c3
# f1c4
# f8c5
# h1f1
# e8f8
# d1e2