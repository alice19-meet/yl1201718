from turtle import *
import random

colormode(255)

class Square(Turtle):
	def __init__(self, size):
		Turtle.__init__(self)
		self.shapesize(size)
		self.shape("square")
	def random_color(self):
		r=random.randint(0,255)
		g=random.randint(0,255)
		b=random.randint(0,255)
		self.color(r,g,b)
s=Square(10)
s.random_color()

class Rectangle(Turtle):
	def __init__(self, height, width):
		Turtle.__init__(self)
		register_shape('rectangle',((height,0),(height,width),(0,width),(0,0)))
		self.shape('rectangle')
		self.setheading(90)
class SQUARE(Rectangle):
	def __init__(self,size):
		Rectangle.__init__(self,size,size)

r=Rectangle(50,100)
S=SQUARE(100)

mainloop()