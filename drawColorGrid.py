import turtle

def drawSquare(myTurtle):
	myTurtle.forward(20)
	myTurtle.right(90)
	myTurtle.forward(20)
	myTurtle.right(90)
	myTurtle.forward(20)
	myTurtle.right(90)
	myTurtle.forward(20)

def drawBlueSquare(myTurtle):
	myTurtle.color('blue')
	drawSquare(myTurtle)
	
def drawRedSquare(myTurtle):
	myTurtle.color('red')
	drawSquare(myTurtle)

def drawYellowSquare(myTurtle):
	myTurtle.color('yellow')
	drawSquare(myTurtle)

def drawGreenSquare(myTurtle):
	myTurtle.color('green')
	drawSquare(myTurtle)	

def squareChain(myTurtle):
	myTurtle.penup()
	myTurtle.left(180)
	myTurtle.forward(20)
	myTurtle.right(90)
	myTurtle.forward(35)
	myTurtle.right(90)
	myTurtle.pendown()


def draw4ColoredSquares(myTurtle):
	drawGreenSquare(myTurtle)
	drawYellowSquare(myTurtle)	
	drawRedSquare(myTurtle)
	drawBlueSquare(myTurtle)

def drawSquareChain(myTurtle):
	count = 0
	while count < 5:
		draw4ColoredSquares(myTurtle)
		squareChain(myTurtle)
		count = count + 1

Bear = turtle.Turtle()

drawSquareChain(Bear)




turtle.exitonclick()
