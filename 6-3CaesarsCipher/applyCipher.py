# applyCipher.py
# A program to encrypt/decrypt user text
# using Caesar's Cipher
#
# Author: rc.bryan [at] leadps.org


# makes a mapping of encoded alphabet to decoded alphabet
# arguments: key
# returns: dictionary of mapped letters
def createDictionary(key):
	# placeholder
	return {}

# Asks for the message that needs to be decoded from the user
# arguments: none
# returns: encoded message
def getMessage():
	pass

# for each letter in message, decodes and records
# arguments: encoded message, dictionary
# returns: decoded message
def decodeMessage(message, dictionary):
	pass
	

# outputs the decoded message to the terminal
# arguments: decoded message
# returns: none
def printMessage(message):
	pass


# execution starts here

# asks user for the key
print("What key would you like to use to decode?")
key = int(raw_input())

dictionary = createDictionary(key)
encodedMessage = getMessage()
decodedMessage = decodeMessage(encodedMessage, dictionary)
printMessage = printMessage(decodedMessage)
