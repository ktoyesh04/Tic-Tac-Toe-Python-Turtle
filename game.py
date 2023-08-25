import random
import os


class Board:
	
	def __init__(self):
		self.board = [['_'] * 3 for _ in range(3)]
	
	def get_current_state(self):
		return self.board
	
	def print_current_state(self):
		self.clear_screen()
		for row in self.board:
			print(' '.join(row))
	
	@staticmethod
	def clear_screen():
		os.system('cls' if os.name == 'nt' else 'clear')


class Game(Board):
	def __init__(self):
		super().__init__()
		self.count = 0
		self.game_over = False
		
	def game_is_on(self):
		return self.count < 9
	
	def set_symbol(self, x: int, y: int, symbol: str):
		self.board[x][y] = symbol
	
	def is_won(self, x: int, y: int, symbol: str) -> bool:
		for i in range(3):
			if self.board[x][i] != symbol:
				break
		else:
			return True
		
		for i in range(3):
			if self.board[i][y] != symbol:
				break
		else:
			return True
		
		if x == y:
			for i in range(3):
				if self.board[i][i] != symbol:
					break
			else:
				return True
		
		if x + y == 2:
			for i in range(3):
				if self.board[i][2 - i] != symbol:
					break
			else:
				return True
		return False
		
	def is_valid_coordinates(self, x: int, y: int) -> bool:
		return 0 <= x <= 2 and 0 <= y <= 2 and self.board[x][y] == '_'
	
	def get_random_coordinates(self):
		while True:
			x, y = random.choice([0, 1, 2]), random.choice([0, 1, 2])
			if self.is_valid_coordinates(x, y):
				return x, y
			
	def check_immediate_win(self, x: int, y: int, symbol: str) -> bool:
		self.set_symbol(x, y, symbol)
		if self.is_won(x, y, symbol):
			self.set_symbol(x, y, '_')
			return True
		self.set_symbol(x, y, '_')
		return False
	
	def check_threat(self, x: int, y: int, user_x: int, user_y: int, user_symbol: str) -> bool:
		mirror_x = 2 * x - user_x
		mirror_y = 2 * y - user_y
		return self.is_valid_coordinates(mirror_x, mirror_y) and self.board[mirror_x-1][mirror_y-1] == user_symbol
	
	def get_bot_coordinates(self, user_x: int, user_y: int, symbol):
		# if self.count < 2:
		# 	return self.get_random_coordinates()

		# check for bot immediate wins
		for x in range(3):
			for y in range(3):
				if self.is_valid_coordinates(x, y) and self.check_immediate_win(x, y, symbol):
					return x, y
		# check for opponents immediate wins
		opponent_symbol = 'O' if symbol == 'X' else 'X'
		for x in range(3):
			for y in range(3):
				if self.is_valid_coordinates(x, y) and self.check_immediate_win(x, y, opponent_symbol):
					return x, y
				
		# threat moves (mirror moves)
		for x in range(3):
			for y in range(3):
				if self.check_threat(x, y, user_x, user_y, opponent_symbol):
					return x, y
				
		# strategical moves based on previous moves
		strategic_moves = [(user_x, user_y), (0, 0), (0, 2), (2, 0), (2, 2)]
		for x, y in strategic_moves:
			if self.is_valid_coordinates(x + 1, y + 1):
				return x + 1, y + 1
		return self.get_random_coordinates()

	def reset_game(self):
		self.count = 0
		self.game_over = False
		self.board = [['_'] * 3 for _ in range(3)]
