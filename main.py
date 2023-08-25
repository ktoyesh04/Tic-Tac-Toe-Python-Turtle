import turtle
from game import Game
from ui import Tim, Screen

SYMBOLS = ('X', 'O')
BOARD_COLOR = '#ffd6ff'


def is_won(x: int, y: int, symbol: str) -> bool:
	if game.is_won(x, y, symbol):
		tim.write_title(f'{symbol} won!')
		screen.screen.onscreenclick(lambda x, y:exit(1))
		return True
	return False


def is_draw():
	if game.count >= 9:
		tim.write_title('Draw!')
		screen.screen.onscreenclick(lambda x, y: exit(1))
		return True


def on_user_click(x: int, y: int):
	x, y = tim.get(x, y)
	if game.is_valid_coordinates(x, y):
		game.set_symbol(x, y, players['User'])
		tim.draw(x, y, players['User'])
		game.count += 1
		if is_won(x, y, players['User']):
			return
		if is_draw():
			return
		tim.write_title(f'Bot: {players["Bot"]}')
		bot_turn(x, y)
		
		
def bot_turn(x: int, y: int):
	x, y = game.get_bot_coordinates(x, y, players['Bot'])
	game.set_symbol(x, y, players['Bot'])
	tim.draw(x, y, players['Bot'])
	game.count += 1
	if is_won(x, y, players['Bot']):
		return
	if is_draw():
		return
	tim.write_title(f'User: {players["User"]}')


tim = Tim()
game = Game()
screen = Screen()
screen.screen.onscreenclick(on_user_click)

x = 0
y = 0

players = {'User': 'X', 'Bot': 'O'}
tim.write_title(f'User: {players["User"]}')
turtle.done()
