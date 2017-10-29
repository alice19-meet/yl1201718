import turtle

turtle.speed(100)
turtle.pensize(6)
turtle.bgcolor('black')
turtle.color('turquoise')

howmanysides=6
sidelength=120
degree=60
howmanysquares=18
angle=20
howmanyshapes=360/angle

for i in range(howmanysquares):
	turtle.left(angle)
	for i in range (howmanysides):
		turtle.forward(sidelength)
		turtle.left(degree)
	


turtle.mainloop()



