
# GLOBAL SECTION - means has access to all functions or methods.

countDict = {}   # It is used to store the frequencies of each noun.

# opens the file in read mode and closes implicitly without writing any close() function.
with open("harrypotter.txt",'r') as file:
	listOfLines = file.readlines() # returns list of lines.

# It splits each line with the help of space character.
for w in range(len(listOfLines)):
	listOfLines[w] = listOfLines[w].split(' ')
# print(listOfLines)




# startwithCapital function checks whether the word is Capitalized or not.
def startWithCapital(word):
	# print(word)
	word = ''.join(e for e in word if e.isalpha()) # return a string without any special character. 
	# below if condition checks whether it is capitalized and has length more than 1 or not.
	if len(word)>1 and word[0].isalpha() and word[0]==word[0].upper():

		# below condition checks whether the dictionary is empty or word is exists in dictionary(coutDict)
		# or not.
		if word not in countDict or countDict == {}:
			countDict[word] = 1

		else:
			countDict[word] += 1

	else:

		# do nothing

		pass

	return countDict



# main function defintion
def main():

	# It iterates each lines each word from starting line.
	for line in range(len(listOfLines)):
		for word in range(len(listOfLines[line])):
			lisword = listOfLines[line][word].strip()		
			startWithCapital(lisword)

	# Used to print the dictionary in reverse sorted order(descending) in accordance to its value.
	print(dict(sorted(countDict.items(),key = lambda x : x[1],reverse = True)))



# main code get called from here
if __name__ == "__main__":
	main()








