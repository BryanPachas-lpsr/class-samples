# open a file for writing
# second argument:
# r is for reading
# r+ is for reading/writing (existing file)
# w is writing (be careful starts writing from the beginning
# a is append - writing *from the end*
my_File = open("numlist.txt", "w")

# create a list to write to my file
nums = range(1,501)


# write each item to the file
for n in nums:
	my_File.write(str(n) + '\n')

my_File.close()
# close the file
