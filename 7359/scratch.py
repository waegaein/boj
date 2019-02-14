import sys


row_min = 1
row_max = 50
col_min = 1
col_max = 50

north = 'N'
south = 'S'
west = 'W'
east = 'E'

msg_success = 'The worm successfully made all %d moves.'
msg_fail_conflict = 'The worm ran into itself on move %d.'
msg_fail_out = 'The worm ran off the board on move %d.'


paths = ['NWWWWWWWWWWSESSSWS', 'SSSWWNENNNNNWWWWSSSS', 'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEE', 'SWWWWWWWWWNEE']


def get_occupied_initial():
	occupied = list()

	for i in reversed(range(11, 31)):
		occupied.append((25, i))

	return occupied


def will_conflict(occupied_head_next, occupied):
	for occupancy in occupied[1:len(occupied) - 1]:
		if occupancy == occupied_head_next:
			return True

	return False


def get_occupied_head_next(current_move, occupied):
	occupied_head = occupied[0]

	if current_move == north:
		return occupied_head[0] - 1, occupied_head[1]
	elif current_move == south:
		return occupied_head[0] + 1, occupied_head[1]
	elif current_move == west:
		return occupied_head[0], occupied_head[1] - 1
	else:
		return occupied_head[0], occupied_head[1] + 1


def will_fail_conflict(current_move, occupied):
	occupied_head_next = get_occupied_head_next(current_move, occupied)

	return will_conflict(occupied_head_next, occupied)


def will_fail_out(current_move, occupied):
	occupied_head = occupied[0]

	if current_move == north:
		return occupied_head[0] == row_min
	elif current_move == south:
		return occupied_head[0] == row_max
	elif current_move == west:
		return occupied_head[1] == col_min
	else:
		return occupied_head[1] == col_max


def get_occupied_next(current_move, occupied):
	occupied_head_next = get_occupied_head_next(current_move, occupied)

	return [occupied_head_next] + occupied[:len(occupied) - 1]


def walk_through(path):
	occupied = get_occupied_initial()

	moves = 0
	while moves != len(path):
		current_move = path[moves]
		moves += 1

		if will_fail_conflict(current_move, occupied):
			print(msg_fail_conflict % moves)
			return
		elif will_fail_out(current_move, occupied):
			print(msg_fail_out % moves)
			return
		else:
			occupied = get_occupied_next(current_move, occupied)

	print(msg_success % moves)


def run():
	#test = '18\nNWWWWWWWWWWSESSSWS\n20\nSSSWWNENNNNNWWWWSSSS\n30\nEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE\n13\nSWWWWWWWWWNEE\n0'
	#for line in test.split('\n'):
	for line in sys.stdin:
		if line.isdigit():
			if int(line) == 0:
				return
		else:
			walk_through(line)


run()
