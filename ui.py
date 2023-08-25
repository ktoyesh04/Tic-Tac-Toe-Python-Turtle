import os
import turtle as t

X_COLOR = '#35155D'
O_COLOR = '#c70339'
BOARD_COLOR = '#ffd6ff'


class Screen:
	def __init__(self):
		self.screen = t.Screen()
		self.screen.setup(width=650, height=650)
		self.screen.title('Tic Tac Toe')
		self.screen.bgpic(os.path.abspath('bg.png'))
		self.screen.bgcolor(BOARD_COLOR)
		
		
class Tim(t.Turtle):
	def __init__(self):
		super().__init__()
		self.x_cor = ((-290, -103, -196.5), (-92, 92, 0), (104, 292, 198))
		self.y_cor = ((91, 257, 174), (-83, 83, 0), (-258, -92, -175))
		
		self.hideturtle()
		self.pensize(4)
		self.speed('fastest')
		self.penup()
		self.title = t.Turtle()
		self.title.hideturtle()
		self.title.penup()

	def write_title(self, text: str) -> None:
		self.title.goto(0, 290)
		self.title.clear()
		self.title.write(f'{text}', align="center", font=("Verdana", 20, "italic"))
	
	def get(self, x: float, y: float) -> tuple[int, int]:
		for i in range(3):
			if self.y_cor[i][0] <= y <= self.y_cor[i][1]:
				for j in range(3):
					if self.x_cor[j][0] <= x <= self.x_cor[j][1]:
						return j, i
	
	# if -290 < x < -103 and 91 < y < 257: # 187, 166
	# 	print('C1')
	# elif -92 < x < 92 and 91 < y < 257: # 184, 166
	# 	print('C2')
	# elif 104 < x < 292 and 91 < y < 257: # 188, 166
	# 	print('C3')
	#
	# elif -290 < x < -103 and -83 < y < 83:
	# 	print('C4')
	# elif -92 < x < 92 and -83 < y < 83:
	# 	print('C5')
	# elif 104 < x < 292 and -83 < y < 83:
	# 	print('C6')
	#
	# elif -290 < x < -103 and -258 < y < -92:
	# 	print('C7')
	# elif -92 < x < 92 and -258 < y < -92:
	# 	print('C8')
	# elif 104 < x < 292 and -258 < y < -92:
	# 	print('C9')
	
	def draw(self, x: int, y: int, symbol: str) -> None:
		c = (self.x_cor[x][2], self.y_cor[y][2])
		if symbol == 'O':
			self.draw_o(c[0], c[1])
		else:
			self.draw_x(c[0], c[1])
	
	def draw_x(self, x: int, y: int) -> None:
		self.pencolor(X_COLOR)
		self.goto(x, y)
		self.setheading(0)
		self.pendown()
		self.left(45)
		self.forward(60)
		self.backward(120)
		self.goto(x, y)
		self.right(90)
		self.forward(60)
		self.backward(120)
		self.penup()

	def draw_o(self, x: int, y: int) -> None:
		self.pencolor(O_COLOR)
		self.goto(x, y - 50)
		self.setheading(0)
		self.pendown()
		self.circle(radius=50)
		self.penup()
