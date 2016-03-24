#Empty list to put prime numbers in
pn = []
#I know I am going to open a file
my_file = open("primenumbers.txt", "w")
#Makes a function that makes labels prime numbers true if they can't be divided evenly into previous numbers. Composite numbers are true
def findprime(num):
	for numba in range(2,num):
		if num % numba == 0:
			return False
	return True
#Uses the function that checks for prime numbers then adds them to a list since the prime numbers return true
for numbers in range(2, 10000):
	#Makes it a variable
	prime = findprime(numbers)
	if prime == True:
		pn.append(numbers)
#Fills the file primenumbers.txt with the prime numbers
my_file.write(str(pn))
#Closes the file
my_file.close()
#Prints the prime numbers in the list
print(pn)

 		 	
