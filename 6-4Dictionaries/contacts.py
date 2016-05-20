contact =  {
	
}



while 5 > 0:
	print("(1) Add a phone number.") 
	print("(2) Print the full list of contacts.") 
	print("(3) Enter a name to retrieve that contact's phone number.") 
	print("(4) Exit the Contacts app")
	x = int(raw_input())
	if x == 1:
		print("Enter contact name:")
		cont = str(raw_input())
		print("Enter number:")
		num = str(raw_input())
		contact[cont] = num
	elif x == 2:
		print("Contacts:")
		print(contact)
	elif x == 3:
		print("Enter name:")
		w = raw_input()
		print("Here is the number:")
		print(contact[w])
		
	elif x == 4:
		exit()


