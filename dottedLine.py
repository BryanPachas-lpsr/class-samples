import turtle



notshawn = turtle.Turtle()

notshawn.speed(1)
count = 0
while count < 100:
	notshawn.forward(5)
        notshawn.penup()
	notshawn.forward(5)
	notshawn.pendown()
	count = count + 1

#go tothe lower left of the scren
notshawn.penup()
notshawn.goto(-100, -55)
#when yo get the draw a circle	
notshawn.pendown()
notshawn.circle(10)












turtle.exitonclick()
