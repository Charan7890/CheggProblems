
# importing os module
from os.path import exists

# readfile function is used to read the content from the file and to print that.
def readfile(fileName):
	k = 0
	with open(fileName,'r') as fp:
		while True:
			if k%2==0:
				line = fp.readline()
				print("Student Name:",line,end="")
			else:
				line = fp.readline()
				print("Performance in exam:",line,end="")

			# In print we used an argument called end="" because, each line implicitly consists of
			# new line character at the end of every line in the file.
			
			#If there is no line exists in the file, then it get terminated.
			if not line:
				break

#readdata function is used to calculate the average marks of the student from a text file.
def readdata(fileName):

	readfile(fileName)

	with open(fileName,'r') as file:
		# It returns list of lines from a file.
		ListOfLines = file.readlines()

	# taking integers from the ListOfLines list(1-D list)
	marks = []

	#print(ListOfLines)-----> ['John Terry\n', '74\n', 'Ashley Cole\n', '33\n', 'Frank Lampard\n', '120\n']
	# Below code converts the string to integer for odd indexed integers in the ListOfLines.
	for i in range(len(ListOfLines)):
		if i%2!=0:
			mark = int(ListOfLines[i])

			marks.append(mark)

	# length of the number of students.
	n = (len(ListOfLines)//2)

	# finding average using the inbuilt functions
	avgMarks = sum(marks)/n

	# round off the two decimal places of the avgMarks variables and reassigns to it.
	avgMarks = round(avgMarks,2)

	print("The average exam score of the "+str(n)+" student in the file<"+fileName+"> is "+str(avgMarks)+".")



# main function implementation
def main():


	# loop to take file name for n - number of times, if user enters wrongly.
	while(True):
		# taking file name from the user
		fileName = input("Please Enter a file name, followed by .txt:")

		# validating whether the file is present in current folder or not.
		# if exists it returns true.
		# else return false.
		value = exists(fileName)

		if value == True:
			print("Checking... "+fileName+" exists in the current directory")
			# readdata() function is called to calculate the average marks of all the students.
			# and also to print the file content.
			readdata(fileName)

			# Here used break, to come out from the loop. Else for other iteration, it may enter
			# into the else case and may create an interuption to an user.
			break

		
		else:
			# case if file doesn't exist.
			# It will get input from user until user enters correct file name.
			print("Checking... "+fileName+" DOES NOT exists in the current directory.Please retry")
			# taking input from the user to come out from the loop.
			exit = int(input("Press 0 to exit, 1 to continue:"))

			if exit==0:
				break

#Program execution starts from here.
if __name__ == "__main__":
	main()
