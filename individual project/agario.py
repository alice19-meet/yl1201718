from turtle import *
import time 
import random
from ball import Ball

tracer(0)

hideturtle()

RUNNING=True
SLEEP=0
SCREEN_WIDTH = getcanvas().winfo_width()/2
SCREEN_HEIGHT = getcanvas().winfo_height()/2

MY_BALL=Ball(0,0,10,50,100,"turquoise")
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


#for i in range (100):
	#move_all_balls()

def collide(ball_a,ball_b):
	if ball_a==ball_b:
		return False
	b1y=ball_a.ycor()
	b2y=ball_b.ycor()
	b1x=ball_b.xcor()
	b2x=ball_a.xcor()
	r1=ball_a.radius
	r2=ball_b.radius
	sr = r1+r2

	d = ((b2x-b1x)**2+(b2y-b1y)**2)**(0.5)
	if d <= sr:
		return True
	else:
		return False

def check_all_balls_colision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if collide(ball_a,ball_b)==True:
				ball_a_radius=ball_a.radius
				ball_b_radius=ball_b.radius
				if ball_a_radius>ball_b_radius:
					x= random.randint(int(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS), int(SCREEN_WIDTH-MAXIMUM_BALL_RADIUS))
					y= random.randint(int(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS), int(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
					dx= random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
					dy= random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
					radius= random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
					color=(random.random(), random.random(), random.random())
					ball_b.goto(x,y)
					ball_b.dx=dx
					ball_b.dy=dy
					ball_b.radius=radius
					ball_b.color("blue")
					ball_a.radius=ball_a.radius+1
					ball_a.shapesize(ball_a_radius/10)
				if ball_b_radius>ball_a_radius:
					x= random.randint(int(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS), int(SCREEN_WIDTH-MAXIMUM_BALL_RADIUS))
					y= random.randint(int(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS), int(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
					dx= random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
					dy= random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
					radius= random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
					color=(random.random(), random.random(), random.random())
					ball_a.goto(x,y)
					ball_a.dx=dx
					ball_a.dy=dy
					ball_a.radius=radius
					ball_a.color("purple")
					ball_b.radius=ball_b.radius+1
					ball_b.shapesize(ball_b_radius/10)

def check_myball_collision():
	for b in BALLS:
		if collide(MY_BALL,b) == True:
			MY_BALL_RADIUS=MY_BALL.radius
			b_radius=b.radius
			if MY_BALL_RADIUS<b_radius:
				return False
			else:
				x= random.randint(int(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS), int(SCREEN_WIDTH-MAXIMUM_BALL_RADIUS))
				y= random.randint(int(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS), int(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
				dx= random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
				dy= random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
				radius= random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
				color=(random.random(), random.random(), random.random())
				b.goto(x,y)
				b.dx=dx
				b.dy=dy
				b.radius=radius
				b.color("pink")
	return True


def movearound (event):
	MY_BALL.goto(event.x-SCREEN_WIDTH,SCREEN_HEIGHT-event.y)

getcanvas().bind("<Motion>", movearound)
getscreen().listen()


while RUNNING== True:
	if SCREEN_WIDTH != getcanvas().winfo_width()/2 and SCREEN_HEIGHT != getcanvas().winfo_height()/2:
		SCREEN_WIDTH = getcanvas().winfo_width()/2
		SCREEN_HEIGHT = getcanvas().winfo_height()/2
	move_all_balls()
	check_all_balls_colision()
	# MY_BALL.move(SCREEN_WIDTH,SCREEN_HEIGHT)
	RUNNING=check_myball_collision()
	getscreen().update()
	time.sleep(0.2)






mainloop()