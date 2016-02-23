# Prints the statements
print("Hello welcome to the Haiku Reader!")
print("Choose")
print("(3) For a haiku about a silly person")
print("(4) For a haiku about writing haikus") 
# Asks for 3 or 4
x = int(raw_input())
if x == 3:
	hai = open('haiku3.txt')
	
elif x == 4:
	hai = open('haiku4.txt')
# Prints a haiku depending on what the user picked
print(hai.read())
hai.close()
