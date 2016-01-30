#Class for defining a class
class Player(object):
	#This is the construcer for the list variables
	def __init__(self, name, age, goals):
		
		self.name = name
		self.age = age
		self.goals = goals
	
	#This prints the stats with string variables to introduce them
	def printStats(self):
		print("name: " + self.name)
		print("age: " + str(self.age))
		print("goals: " + str(self.goals))
		print(" ")
		print("Next Player:")
#Empty player list soon to be filled		
myPlayers = []
#Asks an infinite while statement for what the user will want to do
while 3 > 1:
	print("(1) Add player")
	print("(2) Print players")
	print("(3) Exit Program")
	x = int(raw_input())
	#If x = 1 it asks the user to input player stats
	if x == 1:
		print("Enter Player Name:")
		y = str(raw_input())
		print("Enter Age")
		a = str(raw_input())
		print("Enter Goals")
		b = str(raw_input())
		myPlayers.append(Player(y, a, b,))
	#If x = 2 it prints all the user's player stats
	elif x == 2:
		for g in myPlayers:
			g.printStats()
	#This exits the program
	elif x == 3:
		exit() 

			

			

	
			



