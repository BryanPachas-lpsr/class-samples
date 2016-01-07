import turtle

def drawTee(myTurtle):
	myTurtle.forward(150)
	myTurtle.backward(50)
	myTurtle.right(90)
	myTurtle.forward(50)
	myTurtle.backward(50)
	myTurtle.left(180)
	myTurtle.forward(50)
	myTurtle.backward(50)
	myTurtle.right(90)
	myTurtle.backward(100)
	myTurtle.right(90)

def drawFourTees(myTurtle):
	count = 4
	while count > 0:
		drawTee(myTurtle)
		count = count - 1

# make your turtle down here and pass it to the appropriate places

Bear = turtle.Turtle()
drawFourTees(Bear)
turtle.exitonclick()
