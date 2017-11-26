from turtle import *
speed(1)
class Hexagon(Turtle):
	def __init__(self, size):
		Turtle.__init__(self)
		self.ht()
		self.shapesize(size)
		begin_poly()
		fd(50)
		left(60)
		fd(50)
		left(60)
		fd(50)
		left(60)
		fd(50)
		left(60)
		fd(50)
		left(60)
		fd(50)
		
		end_poly()
		p = get_poly()
		register_shape('hexagon', p)
		self.shape("hexagon")
		self.showturtle()

h=Hexagon(10)