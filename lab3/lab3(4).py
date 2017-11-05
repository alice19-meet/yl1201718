import turtle
angle = 5
for i in range(125):
	turtle.speed(1000000000000000000000000)
	turtle.forward(200)
	turtle.right(25)
	turtle.forward(50)
	turtle.right(90)
	turtle.forward(50)
	turtle.home()
	turtle.right(angle)
	angle = angle+3

turtle.mainloop()