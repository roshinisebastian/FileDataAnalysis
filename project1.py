''' Write a program that reads the file and reports statistics on the file'''


def main():
	LETTERS = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	inputFile = input('Enter the file name that has to be processed: ')
	print ('The name of the file is: ', inputFile)
	outputFile = input('Enter the output file name: ')
	print ('The name of the output file is: ', inputFile)
	countLetters = {}
	globalCount = 0
	frequencyLetters = {}
	wordCount = {}

	try:
		infile = open(inputFile,'r')
		outfile = open(outputFile,'w')
	except FileNotFoundError as fileErr:
		print(fileErr)
	else:
		content = infile.read()
		content.lower()
		newContent = content.replace(' ','')
		globalCount = len(newContent)
		newStr = 'The count of the non white space characters in the file '+inputFile+' is: ' + str(len(newContent)) + '\n\n'
		outfile.write(newStr)
	
		countLetters = countFrequency(content,LETTERS)
		newStr = 'The count of the letters in the file '+inputFile+' is: \n' 
		outfile.write(newStr)
	
		for key in countLetters:
			freq = (countLetters[key] / globalCount ) * 100.0
			newStr = 'Character = ' + key + ' ' +'Count = ' + str(countLetters[key]) + ' '+'Frequency = ' + str(freq) + '\n'
			outfile.write(newStr)
	
		listOfWords = content.split()
		newStr = '\nThe count of the words in the file '+inputFile+' is: ' + str(len(listOfWords))+ '\n'
		outfile.write(newStr)
	
		for words in listOfWords:
			if words in wordCount:
				count = wordCount[words]
				count = count + 1
				newDict = {words:count}
				wordCount.update(newDict)
			else:
				newDict = {words:1}
				wordCount.update(newDict)
		newStr = '\nThe top 10 words in the file '+inputFile+' is:' 
		outfile.write(newStr)
		for w in sorted(wordCount, key=wordCount.get, reverse=True):
			newStr = '\nWord = ' + w + '\tCount = ' + str(wordCount[w])
			outfile.write(newStr)
	
	finally:
		infile.close()
		outfile.close()
		
def countFrequency(content,LETTERS):
	countLetter = {}
	for letter in LETTERS:
		count = content.count(letter)
		newDict = {letter:count}
		countLetter.update(newDict)
	return countLetter
		
main()