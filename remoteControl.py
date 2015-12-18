import turtle
from Tkinter import *
f = turtle.Turtle()
x = 3
def a(f):
	while x > 3:
		f.forward(100)
		f.left(120)
		x = x - 1
aj = Button(frame, text='tri', command =lambda: f.a())
aj.pack(side=LEFT)







# create the root Tkinter window and a Frame to go in it
root = Tk()
frame = Frame(root)

# create our turtle
shawn = turtle.Turtle()

# make some simple buttons
fwd = Button(frame, text='fwd', command=lambda: shawn.forward(50))
bwd = Button(frame, text='bwd', command=lambda: shawn.backward(50))
left = Button(frame, text='left', command=lambda: shawn.left(90))
right = Button(frame, text='right', command=lambda: shawn.right(90))
penup = Button(frame, text='penup', command=lambda: shawn.penup())
pendown = Button(frame, text='pendown', command=lambda: shawn.pendown())
# put it all together
fwd.pack(side=LEFT)
bwd.pack(side=LEFT)
left.pack(side=LEFT)
right.pack(side=LEFT)
penup.pack(side=LEFT)
pendown.pack(side=LEFT)
frame.pack()

turtle.exitonclick()
