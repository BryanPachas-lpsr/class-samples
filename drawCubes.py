import turtle
#makes a regular rhombus
def drawRegRhombus(myTurtle):
	myTurtle.fillcolor("light blue")
	myTurtle.begin_fill()
	myTurtle.right(60)
	myTurtle.forward(20)
	myTurtle.right(120)
	myTurtle.forward(20)
	myTurtle.right(60)
	myTurtle.forward(20)
	myTurtle.right(120)
	myTurtle.forward(20)
	myTurtle.end_fill()
#makes the opposite of the rhombus
def drawOtherRhombus(myTurtle):
	myTurtle.fillcolor("dark cyan")
	myTurtle.begin_fill()
	myTurtle.right(60)	
        myTurtle.forward(20)
        myTurtle.left(120)
        myTurtle.forward(20)
        myTurtle.left(60)
        myTurtle.forward(20)
        myTurtle.left(120)
        myTurtle.forward(20)
	myTurtle.end_fill()
#Makes the top rhombus
def drawTopRhombus(myTurtle):
	myTurtle.fillcolor("dark blue")
	myTurtle.begin_fill()
	myTurtle.right(30)
	myTurtle.left(60)
	myTurtle.forward(20)
	myTurtle.left(120)
	myTurtle.forward(20)
	myTurtle.left(60)
	myTurtle.forward(20)
	myTurtle.left(120)
	myTurtle.forward(20)
	myTurtle.end_fill()	
#Makes a cube
def drawCube(myTurtle):
	
	drawTopRhombus(myTurtle)
	drawRegRhombus(myTurtle)
	drawOtherRhombus(myTurtle)
#Places the cube side by side eachother
def drawPlacementofCubes(myTurtle):
	drawCube(myTurtle)
	myTurtle.penup()
	myTurtle.right(210)
	myTurtle.forward(34)	
	myTurtle.pendown()
#Draws a row of cubes
def drawCompleteRowofCubes(myTurtle):
	count = 0
	while count < 4:
		drawPlacementofCubes(myTurtle)
		count = count + 1
	drawCube(myTurtle)
#Prepares the next line
def nextLine(myTurtle):
	myTurtle.speed(0)	
	drawCompleteRowofCubes(myTurtle)
	myTurtle.penup()
	myTurtle.goto(0,0)
	myTurtle.pendown()		
	myTurtle.right(60)
	myTurtle.forward(20)
	myTurtle.right(120)
	myTurtle.forward(20)
	myTurtle.right(60)
	myTurtle.penup()
	myTurtle.forward(20)
	myTurtle.left(120)
	myTurtle.forward(20)
	myTurtle.right(90)
	myTurtle.pendown()	
	drawCompleteRowofCubes(myTurtle)
	positioning(myTurtle)
	positioning(myTurtle)
#Positions the turtle to make more cube rows
def positioning(myTurtle):
	myTurtle.penup()
	myTurtle.right(30)
	#rememeber 85
	myTurtle.forward(137)
	myTurtle.left(30)
	myTurtle.right(60)
        myTurtle.forward(20)
        myTurtle.right(120)
        myTurtle.forward(20)
        myTurtle.right(60)
        myTurtle.forward(20)
        myTurtle.left(120)
        myTurtle.forward(20)
        myTurtle.right(90)
        myTurtle.pendown()
	drawCompleteRowofCubes(myTurtle)
#Puts the functions on the turtle "Bear"
Bear = turtle.Turtle()
nextLine(Bear)
turtle.exitonclick()
