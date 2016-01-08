import turtle

def makeTriangle(myTurtle): 	
	myTurtle.forward(10)
	myTurtle.left(120)
	myTurtle.forward(10)
	myTurtle.left(120)
	myTurtle.forward(10)
	myTurtle.left(120)
		

def make4Triangle(myTurtle):
	myTurtle.penup()
	myTurtle.forward(30)
	myTurtle.pendown()

def changeAngle(myTurtle):
	myTurtle.penup()
	myTurtle.goto(0,0)
	myTurtle.pendown()
	myTurtle.left(30)



Bear = turtle.Turtle()


def oneSet(myTurtle):
	count = 0
	while count < 4:
		makeTriangle(myTurtle)
		make4Triangle(myTurtle)
		count = count + 1


def All(myTurtle):
	num = 0
	while num < 3:
		oneSet(myTurtle)
		changeAngle(myTurtle)
		num = num + 1
def All2(myTurtle):
	All(myTurtle)
	myTurtle.goto(0,0)
	myTurtle.left(100)
	All(myTurtle)

All2(Bear)


	
	
turtle.exitonclick()
