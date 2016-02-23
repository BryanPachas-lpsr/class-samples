
# Welcomes the user
print("Welcome to the Haiku generator!")
# Asks user for input in first,second, and third line of haiku
print("Provide the first line of your haiku:")
x = str(raw_input())
print("Provide the second line of your haiku:")
y = str(raw_input())
print("Provide the third line of your haiku:")
z = str(raw_input())
# Asks for name of haiku file
print("What file would you like to write your haiku to?")
# Makes a list to put the user input in
my_File = []
my_File.append(x)
my_File.append(y)
my_File.append(z)
# "nameHaiku" is made into file and has its name changed to user input
nameHaiku = raw_input() 

new_File = open(nameHaiku, "a")
# Prints each line separately for each line in the file
for count in my_File:
	new_File.write(count + "\n")
# Tells the user how to view their haiku in their new file
print("Done! To view your haiku, type 'cat' and the name of your file at the command line.")
