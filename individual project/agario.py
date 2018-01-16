from turtle import *
import time 
import random
from ball import Ball

#tracer(0)

#hideturtle()

RUNNING=True
SLEEP=0
SCREEN_WIDTH = getcanvas().winfo_width()/2
SCREEN_HEIGHT = getcanvas().winfo_height()/2

my_ball=Ball(0,0,10,50,100,"turquoise")
NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5
BALLS=[]


for i in range(NUMBER_OF_BALLS):
	x= random.randint(int(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS), int(SCREEN_WIDTH-MAXIMUM_BALL_RADIUS))
	y= random.randint(int(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS), int(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
	dx= random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	dy= random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
	radius= random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
	color=(random.random(), random.random(), random.random())
	ball1=Ball(x,y,dx,dy,radius,color)
	BALLS.append(ball1)


def move_all_balls():
	for b in BALLS:
		b.move(SCREEN_WIDTH,SCREEN_HEIGHT)

def collide(ball_a,ball_b):
	if ball_a==ball_b:
		return False
	b1y=ball1.ycor()
	b2y=my_ball.ycor()
	b1x=my_ball.xcor()
	b2x=ball1.xcor()
	sr = r1+r2
	d = ((b2x-b1x)**2+(b2y-b1y)**2)**(0.5)
	if d <= sr:
		return True
	else:
		return False




mainloop()