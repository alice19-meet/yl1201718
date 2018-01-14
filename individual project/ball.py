from turtle import *
import random
import math

colormode (255)
tracer(0)
hideturtle()

class Ball(Turtle):
	def __init__(self,x,y,dx,dy,radius,color):
		Turtle.__init__(self)
		self.pu()
		self.goto(x,y)
		self.dx = dx
		self.dy = dy
		self.shape("circle")
		self.radius=radius
		self.shapesize(radius/10)
		self.color(color)
		
		
	def move(self,screen_width,screen_height):
		current_x=self.xcor()
		current_y=self.ycor()
		new_x=current_x+self.dx
		new_y=current_y+self.dy
		right_side_ball=new_x+self.radius
		left_side_ball=new_x-self.radius
		top_side_ball=new_y+self.radius
		bottom_side_ball=new_y-self.radius
		right_edge=screen_width/2
		left_edge=-screen_width/2
		top_edge=screen_height/2
		bottom_edge=screen_height/2
		self.goto(new_x,new_y)

	if right_side_ball>