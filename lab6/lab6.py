from turtle import *
import random
import math
import turtle

class Ball(Turtle):
	def __init__(self,radius,color,speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius)
		self.color(color)
		self.speed(speed)

ball1=Ball(7,"blue",1)
ball2=Ball(10,"red",1)
ball1.goto(100,100)
ball2.goto(-100,-100)
ball1.goto(-100,-100)
#ball_x=ball.xcor()
#ball_y=ball.cor()
#ball2_x=ball.xcor()
#ball2_y=ball.ycor()


def check_collision(ball1,ball2):
	if (ball1.shapesize()[0])+ball2.shapesize()[0]>(math.sqrt(math.pow(ball1.xcor()-ball2.ycor(),2)+(math.pow(ball1.ycor()-ball2.ycor(),2)))):
		print("collision")
		turtle.write('collision')

check_collision(ball1,ball2)

turtle.mainloop()