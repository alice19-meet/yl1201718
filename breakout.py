from turtle import *
import random
import turtle
import time
from block import Block
from ball import Ball
import math


#tracer(0)
# hideturtle()


		
	

MY_BALL=Ball(0,0,0,0,10,"turquoise")
MY_BALL.goto(0,-SCREEN_HEIGHT+30)


   
t=20
l=-290
SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2
BLOCKS=[]
NUMBER_OF_BLOCKS_LINE=9
NUMBER_OF_BLOCKS_COLUMN=10
for i in range(NUMBER_OF_BLOCKS_COLUMN):
    color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    for g in range(NUMBER_OF_BLOCKS_LINE):
   	 x=l
   	 y=SCREEN_HEIGHT-t
   	 new_block=Block(x,y,color)
   	 BLOCKS.append(new_block)
   	 l=l+70
    t=t+25
    l=-290


def collision(ball_a,block_a):
	if(
	ball_a.top() >= block_a.bottom() and
	ball_a.right() >= block_a.left() and
	ball_a.bottom() <= block_a.top() and
	ball_a.left() <= block_a.right()
	):
		return collision


	


def check_myball_collision():
	global score , score_total
	for b in BLOCKS:
		if collission(MY_BALL,b) == True:
			MY_BALL_RADIUS=MY_BALL.radius
			b_radius=b.radius
			if MY_BALL_RADIUS<b_radius:
				x= random.randint(int(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS), int(SCREEN_WIDTH-MAXIMUM_BALL_RADIUS))
				y= random.randint(int(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS), int(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
				dx= random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
				dy= random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
				while dx==0:
					dx= random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
				while dy==0:
					dy=random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
				radius= random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
				color=(random.random(), random.random(), random.random())
				b.goto(x,y)
				b.dx=dx
				b.dy=dy
				b.radius=radius
				b.shapesize(b.radius/10)
				return False
			else:
				if score == 100:
					print("YOU WIN")
					score_total.pu()
					score_total.goto(0,250)
					score_total.clear()
					score_total.write("SCORE: "+str(score),align="center",font=("Arial",20,"normal"))
					score_total.goto(0,0)
					score_total.write("YOU WIN"+str(score),align="center",font=("Arial",80,"normal"))
					time.sleep(0.9)
					turtle.bye()


				else:
					score+=1 
					score_total.pu()
					score_total.goto(0,250)
					score_total.clear()
					score_total.write("SCORE: "+str(score),align="center",font=("Arial",20,"normal"))
					x= random.randint(int(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS), int(SCREEN_WIDTH-MAXIMUM_BALL_RADIUS))
					y= random.randint(int(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS), int(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
					dx= random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
					dy= random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
					while dx==0:
						dx= random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
					while dy==0:
						dy=random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
					radius= random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
					color=(random.random(), random.random(), random.random())
					b.goto(x,y)
					
					b.dx=dx
					b.dy=dy
					b.radius=radius
					b.shapesize(b.radius/10)
					MY_BALL.radius+=1
					print(MY_BALL_RADIUS)
					MY_BALL.shapesize(MY_BALL_RADIUS/10)

time.sleep(2)