#Class for defining a class
class Player(object):
        #This is the construcer for the list variables
        def __init__(self, name, age, goals, jerseynumber, position):
 
                self.name = name
                self.age = age
                self.goals = goals
		self.jerseynumber = jerseynumber
		self.position = position 
        #This prints the stats with string variables to introduce them
        def printStats(self):
                print("name: " + self.name)
                print("age: " + str(self.age))
                print("goals: " + str(self.goals))
                print("jersey number: " + str(self.jerseynumber))
		print("position: " + str(self.position))
		print(" ")
                print("Next Player:")
#Empty player list sooned to be filled
myPlayers = []
#Function that saves the teeam into a file.
def saveTeam(myPlayers, filename):
	#Opens the file
	user_file = open(filename, 'a')
	#Writes to the file the name, age, goal, jerseynumber, and position fo each player 
	for peep in myPlayers:
		user_file.write(peep.name + " " + str(peep.age) + " " + str(peep.goals) + " " + str(peep.jerseynumber) + " " + peep.position + '\n') 
	user_file.close()



#Function that loads the stats of each player from the tmd file
def loadFile(filename):	
	#List for placing players inside
	teamList = []
	user_file = open(filename, 'r')
	team_file = user_file.readline()
	#Creates a while loop to append every player and their stats
	while team_file != "":
		new_file = team_file.split()
		#Adds the players to the file 
		teamList.append(Player(new_file[0], new_file[1], new_file[2], new_file[3], new_file[4]))
		#Reads every line on separate lines
		team_file = user_file.readline()
	user_file.close()
	#Returns whats in the list I DONT THINK THIS PART IS WORKING
	return teamList











#Asks an infinite while statement for what the user will want to do
print("Welcome to Team Manager Deluxe")
print("Do you want to start with a new team or open an existing team?")
print("(1) Start with a new team")
print("(2) Open a file for an existing team")
user_input = int(raw_input())
if user_input == 1:
	while 3 > 1:
        	print("(1) Add player")
        	print("(2) Print players")
        	print("(3) Save your player list to a file")
		print("(0) Exit Program")
        	x = int(raw_input())
        	#If x = 1 it asks the user to input player stats
        	if x == 1:
               		print("Enter Player Name:")
               		y = str(raw_input())
               		print("Enter Age")
               		a = str(raw_input())
               		print("Enter Goals")
               		b = str(raw_input())
               		print("Jersey Number")
			c = str(raw_input())
			print("Position")
			d = str(raw_input())
			myPlayers.append(Player(y, a, b, c, d))
        	#If x = 2 it prints all the user's player stats
        	elif x == 2:
               		for g in myPlayers:
                        		g.printStats()
 			
		elif x == 3:
			print("Enter the name of the file you want to save your players in, include its .tmd extension.")
			saving_file = raw_input()
			saveTeam(myPlayers, saving_file)

			

		#This exits the program
        	elif x == 0:
                	exit() 
#Asks forthe filename to put in the function
elif user_input == 2:
	print("What's the filename for your existing team? Enter the whole name, including its .tmd extension.")
	filename = raw_input()	
	myPlayers = loadFile(filename)
	#Goes through this loop again after .tmd file is loaded
	while 3 > 1:
                print("(1) Add player")
                print("(2) Print players")
                print("(3) Save your player list to a file")
                print("(0) Exit Program")
                x = int(raw_input())
                #If x = 1 it asks the user to input player stats
                if x == 1:
                        print("Enter Player Name:")
                        y = str(raw_input())
                        print("Enter Age")
                        a = str(raw_input())
                        print("Enter Goals")
                        b = str(raw_input())
                        print("Jersey Number")
                        c = str(raw_input())
                        print("Position")
                        d = str(raw_input())
                        myPlayers.append(Player(y, a, b, c, d))
                #If x = 2 it prints all the user's player stats
                elif x == 2:
			print("Here are all the players:")
			for g in myPlayers:
                                        g.printStats()
 		#Saves the file into a newly created file with a name that the user can give
                elif x == 3:
                        print("Enter the name of the file you want to save your players in, include its .tmd extension.")
                        saving_file = raw_input()
                        saveTeam(myPlayers, saving_file)
		#This exits the program
		elif x == 0:
			exit()
